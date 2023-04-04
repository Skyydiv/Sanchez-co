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
            

#class IAevitecrash:
    """
    sous-classe de l'IA permettant permettant d'eviter au robot de se crash 
    """
 #   def __init__(self,controleur, v):
  #      self.CR=controleur
#        self.tourner=IATournerAngle(controleur,90,v)
 #       self.en_cours=False
  #      
   # def start(self):
    #    self.CR.resetDistanceParcourue()
     #   self.en_cours=True
      #  self.CR.tournerDroite(self.v)
       # 
    ##   #On ne s'arrête que si on l'a depassé l'angle 
      #  return self.CR.AngleParcouru > abs(self.angle) 
        
    #def update(self, delta_t):
        


class IAevitecrash:
    """
    sous-classe de l'IA permettant permettant d'eviter au robot de se crash 
    """
    def __init__(self, robot, v):
        
        self.robot = robot
        self.running = False
        self.v = v
        self.parcouru_g = 0
        self.parcouru_d = 0
        #Calcul de la distance à l'obstacle le plus proche
        self.distance = self.robot.capteur.getDistcapteur_distanceance()



    def start(self):
        if not self.running:
            self.running = True
            self.parcouru_g = 0
            self.parcouru_d = 0
            
        

    def stop(self):
        #Avance vers l'obstacle/mur jusqu'à être à une distance de sécurité
        return self.parcouru_g  - self.distance <= 1 or self.parcouru_d - self.distance <= 1

    
    def end(self):
        self.robot.setVitesse(0,0)
        self.parcouru_g = 0
        self.parcouru_d = 0

    def update(self, delta_t):
        self.CR.update(delta_t)
        if self.running:
            parcouru_g, parcouru_d = self.robot.get_distance_roue(delta_t)
            self.parcouru_g += parcouru_g
            self.parcouru_d += parcouru_d
            if self.stop(): 
                self.end()
                return
            else:
                self.robot.setVitesse(self.v,self.v)
   
        
        
        
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
    iaa=IATournerAngle(controleur,90,vitesse*3)

#ia pour eviter un crash
    iaec = IAevitecrash(controleur, 5, ia1, iaa)




#ia seq 
    iacarre=IAseq(controleur,[iaec,iaa,iaec,iaa,iaec,iaa,iaec,iaa])

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

    def __init__(self, controleur, distance_min, ia_avancer, ia_tourner):
        self.CR = controleur
        self.distance_min = distance_min
        self.ia_avancer = ia_avancer
        self.ia_tourner = ia_tourner
        self.en_cours = False

    def is_near_obstacle(self):
        distance = self.controleur.get_distance()
        return distance <= self.distance_min

    def start(self):
        ia_if_then_else = IAIfThenElse(self.controleur, self.is_near_obstacle, self.ia_tourner, self.ia_avancer)
        ia_if_then_else.start()
        self.en_cours = True


    def stop(self):
        self.ia_if_then_else.stop()
        self.en_cours = False

    def update(self, delta_t):
        self.ia_if_then_else.update(delta_t)
        if not self.ia_if_then_else.en_cours:
            self.stop()