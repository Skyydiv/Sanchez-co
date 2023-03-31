from abc import ABC, abstractmethod
import math
from time import sleep
from time import time
from threading import Thread
from .controleur import ControleurRobotVirtuel


#plus de abstract
class BoucleIA(Thread):
    
    def __init__(self, controleur, ia,delta_t):
        Thread.__init__(self)
        self.controleur = controleur
        self.ia=ia
        self.delta_t=delta_t


    def run(self):
        self.ia.start()
        self.controleur.reset_time()
        while self.ia.en_cours:
            self.ia.update(self.controleur.temps_total)
            sleep(self.delta_t)

class Ia_Avancer_tout_droit:
    
    def __init__(self, distance, v, controleur):

        self.goal = distance
        self.v = v
        self.en_cours=False
        self.CR=controleur
       
        
    def start(self):
        self.en_cours=True
        self.CR.avancerToutDroit(self.v)
       
 
    def stop(self):
        # Si l'une des roues a parcouru plus que la distance à parcourir, arrêter le robot
        if (self.CR.distanceParcourue)>= self.goal:
            return True 
        return False
    
    
    def update(self, delta_t):
        if self.stop():
            self.CR.resetDistanceParcourue()
            self.CR.stop()
            self.en_cours=False
            
        else:
            self.CR.update()
            self.CR.avancerToutDroit(self.v)
    
          
    
class IATournerAngle:
    """
    Classe IA pour tourner d'un certain angle a vers la droite
    """
    def __init__(self, controleur, angle, vitesse):
        
        self.angle = math.radians(angle) 
        #on convertit les degrés passés en paramètre en radians pour les calculs
        self.CR=controleur
        self.en_cours=False
        self.v=vitesse

    def start(self):
        self.CR.resetDistanceParcourue()
        self.en_cours=True
        self.CR.tournerDroite(self.v)
        
    def stop(self):
        #On ne s'arrête que si on l'a depassé l'angle 
        return self.CR.angleParcouru > abs(self.angle) 
        
    def update(self, delta_t):
        #Calcul de l'angle parcouru
        if self.stop():
            self.en_cours=False
            self.CR.stop()
            self.CR.resetAngleParcourue()

        else:
            self.CR.update()
            self.CR.tournerDroite(self.v)
            
   
    
class IAseq:
        """
            sous classe d'IA permettant de lancer une liste d'IA à la suite
         """
        
        def __init__(self,controleur,liste):
            self.CR=controleur
            self.ia_list=liste
            self.en_cours=False
            self.ia_en_cours=0
            
        def start(self):
            self.en_cours=True
            self.ia_list[self.ia_en_cours].start()
            
        def stop(self):
            if not (self.ia_list[self.ia_en_cours].en_cours):
                self.ia_en_cours+=1
                if self.ia_en_cours>=len(self.ia_list):
                    self.en_cours=False
                    return True
                else:
                    self.ia_list[self.ia_en_cours].start()
                    return False
            return False
        
        def update(self, delta_t):
            if self.stop():
                self.CR.stop()
                self.en_cours=False
                self.ia_en_cours=0
                
            else:
                self.ia_list[self.ia_en_cours].update(delta_t)



def TracerCarre(controleur,distance,vitesse):



#ia pour avancer tout droit 
    ia1=Ia_Avancer_tout_droit(distance,vitesse,controleur)

#ia pour tourner 
    iaa=IATournerAngle(controleur,90,vitesse)

#ia seq 
    iacarre=IAseq(controleur,[ia1,iaa,ia1,iaa,ia1,iaa,ia1,iaa])

    return iacarre



class IAIfThenElse:
    """
    sous classe d'IA évaluant une condition et ne faisant rien si elle est fausse
    """
    def __init__(self, controleur, condition, ia_then, ia_else=None):
        self.CR = controleur
        self.condition = condition
        self.ia_then = ia_then
        self.ia_else = ia_else
        self.en_cours = False

    def start(self):
        self.en_cours = True
        if self.condition():
            self.current_ia = self.ia_then
        else:
            self.current_ia = self.ia_else
        if self.current_ia:
            self.current_ia.start()

    def stop(self):
        return not self.current_ia or not self.current_ia.en_cours

    def update(self, delta_t):
        if self.stop():
            self.en_cours = False
            if self.current_ia:
                self.current_ia.stop()
                self.current_ia = None
        else:
            self.current_ia.update(delta_t)
            
class IAevitecrash:
    """ 
    sous classe d'IA permettant d'éviter un obstacle en tournant à droite
    """
    def __init__(self, controleur, distance_limite, vitesse):
        self.CR = controleur
        self.distance_limite = distance_limite
        self.vitesse = vitesse
        self.ia_tourner_droite = IATournerAngle(controleur, 90, vitesse)

        def condition_proximite():
            distance_obstacle = self.CR.get_distance()
            return distance_obstacle <= self.distance_limite

        self.ia_if_then_else = IAIfThenElse(condition_proximite, self.ia_tourner_droite, None)
        self.en_cours = False

    def start(self):
        self.en_cours = True
        self.ia_if_then_else.start()

    def stop(self):
        self.ia_if_then_else.stop()
        self.en_cours = False

    def update(self, delta_t):
        self.ia_if_then_else.update(delta_t)
        if not self.ia_if_then_else.en_cours:
            self.stop()
