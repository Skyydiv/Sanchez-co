from abc import ABC, abstractmethod
import math
from time import sleep
from threading import Thread
from .controleur import ControleurRobotVirtuel


#plus de abstract
class BoucleIA(Thread):
    
    def __init__(self, controleur, ia):
        Thread.__init__(self)
        self.controleur = controleur
        self.ia=ia
        self.delta_t =1./100

    def run(self):
        self.ia.start()
        self.controleur.running = True
        while self.ia.en_cours:
            #---------------------------
            self.ia.update(self.delta_t)
            sleep(self.delta_t)
        self.controleur.running = False

class Ia_Avancer_tout_droit:
    
    def __init__(self, robot, distance, v, controleur):

        self.robot = robot
        self.parcouru_gauche=0
        self.parcouru_droite=0
        self.goal = distance
        self.v = v
        self.en_cours=False
        self.delta_t=1./100
        self.CR=controleur
       
        
    def start(self):
        self.parcouru_gauche=0
        self.parcouru_droite=0
        self.en_cours=True
        self.CR.avancerToutDroit(self.v)
       
 
    def stop(self):
         # Si l'une des roues a parcouru plus que la distance à parcourir, arrêter le robot
        if (self.CR.distanceParcourue)>= self.goal:
            return True 
        return False
    
    
    def update(self, delta_t):
        if self.stop():
            self.parcouru_gauche = 0
            self.parcouru_droite = 0
            self.CR.stop()
            self.en_cours=False
            print("fin de l'ordre")
            
        else:
            self.CR.calculDistanceParcourue(delta_t)
    
          
    
class IATournerAngle:
    """
    Classe IA pour tourner d'un certain angle a vers la droite
    """
    def __init__(self, controleur, angle, vitesse):
        
        Thread.__init__(self)
        
        self.angle = math.radians(angle)
        self._controleur=controleur
        self.threadIA=Thread(target=self.boucleIA)
        
        if angle >= 0:
            self.vitesse = vitesse
        else:
            self.vitesse = -vitesse
        self.parcouru = 0

    def start(self):
        self.parcouru = 0
        self._controleur.calculAngleParcouru()
        threadIA=Thread(target=self.boucleIA)
        threadIA.start()
        
    def stop(self):
        #On ne s'arrête que si on l'a depassé l'angle 
        return self.parcouru > abs(self.angle) 
        
    def update(self, dT : float):
        #Calcul de l'angle parcouru
        a = abs(self._controleur.calculAngleParcouru())
        self.parcouru += a
        
        if self.stop():
            self.end()
            print("fin de l'ordre")
            self._controleur.stop()
            return

        self.avancer()

    def end(self):
        self._controleur.SetVitesseRoues(0,0)

    def avancer(self):
        self._controleur.SetVitesseRoues(self.vitesse,-self.vitesse)
    

    
class IAseq:
    """
    sequence de sous IA 
    """
    def __init__(self, listeIA):
        
        self.listeIA = listeIA
        self.curr = 0



    def start(self):
        pass


    def stop(self):
        if self.curr == len(self.listeIA):
            return True
        
        
    def update(self):
        if self.stop():
            return
        else:
            self.listeIA[self.curr].stop()
            self.curr+=1
            self.listeIA[self.curr].start()
        self.listeIA[self.curr].update()
    


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
        if self.running:
            parcouru_g, parcouru_d = self.robot.get_distance_roue(delta_t)
            self.parcouru_g += parcouru_g
            self.parcouru_d += parcouru_d
            if self.stop(): 
                self.end()
                return
            else:
                self.robot.setVitesse(self.v,self.v)
   
        
        
        
    