from abc import ABC, abstractmethod
import math
from time import sleep
from time import time
from threading import Thread
from .controleur import Controleur


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
       
    def update(self, delta_t):
        if self.stop():
            self.CR.resetDistanceParcourue()
            self.CR.stop()
            self.en_cours=False
            
        else:
            self.CR.update()
            self.CR.avancerToutDroit(self.v)
        
    def stop(self):
        # Si l'une des roues a parcouru plus que la distance à parcourir, arrêter le robot
        if (self.CR.distanceParcourue)>= self.goal:
            return True 
        return False
    
class Ia_Cercle:
    
    def __init__(self, vg, vd, controleur):
        self.CR=controleur
        self.vg=vg
        self.vd=vd
        #calcule le rayon du cercle de rotation
        self.r = ((self.CR.robot.WHEEL_BASE_WIDTH/2) * (self.vg + self.vd)) / abs(self.vd - self.vg)
        #calcule le circonférence du cercle de rotation
        self.goal=2*math.pi*self.r
        self.en_cours=False
       
        
    def start(self):
        self.en_cours=True
       
 
    def stop(self):
        # Si l'une des roues a parcouru plus que la distance à parcourir, arrêter le robot
        if (self.CR.distanceParcourue)>self.goal:
            return True 
        return False
    
    
    def update(self, delta_t):
        if self.stop():
            self.CR.resetDistanceParcourue()
            self.CR.stop()
            self.en_cours=False
            
        else:
            self.CR.update()
            self.CR.setVitesseRoues(self.vg, self.vd)
    
          
    
class IATournerAngleDroite:
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
        self.CR.resetAngleParcourue()
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
            
class IATournerAngleGauche:
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
        self.CR.resetAngleParcourue()
        self.en_cours=True
        self.CR.tournerGauche(self.v)
    def stop(self):
        #On ne s'arrête que si on l'a depassé l'angle 
        return -(self.CR.angleParcouru)>  self.angle
        
    def update(self, delta_t):
        #Calcul de l'angle parcouru
        if self.stop():
            self.en_cours=False
            self.CR.stop()
            self.CR.resetAngleParcourue()

        else:
            self.CR.update()
            self.CR.tournerGauche(self.v)
            

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
        

class IA_led:
    def __init__(self, distance, v, controleur):

        self.goal = distance
        self.v = v
        self.en_cours=False
        self.CR=controleur
       
        
    def start(self):
        self.en_cours=True
        self.CR.robot.set_led(1,True)
        self.CR.avancerToutDroit(self.v)
       
    def update(self, delta_t):
        if self.stop():
            self.CR.resetDistanceParcourue()
            self.CR.stop()
            self.en_cours=False
            
        else:
            if self.CR.robot.led1==False and self.CR.robot.led2==False:
                self.CR.robot.set_led(1,True)
                self.CR.robot.set_led(2,True)

            elif self.CR.robot.led1==True and self.CR.robot.led2==False:
                self.CR.robot.set_led(1,False)
                self.CR.robot.set_led(2,True)

            elif self.CR.robot.led1==False and self.CR.robot.led2==True:
                self.CR.robot.set_led(1,True)
                self.CR.robot.set_led(2,False)
            else:
                self.CR.robot.set_led(2,False)
                self.CR.robot.set_led(1,False)
            self.CR.update()
            self.CR.avancerToutDroit(self.v)
        
    def stop(self):
        # Si l'une des roues a parcouru plus que la distance à parcourir, arrêter le robot
        if (self.CR.distanceParcourue)>= self.goal:
            return True 
        return False

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
    iaa=IATournerAngleDroite(controleur,90,vitesse)

#ia seq 
    iacarre=IAseq(controleur,[ia1,iaa,ia1,iaa,ia1,iaa,ia1,iaa])

    return iacarre

def Strategiemotif1(controleur,distance,vitesse):
    ia1=Ia_Avancer_tout_droit(distance,vitesse,controleur)
    ia2=IATournerAngleGauche(controleur,45,vitesse)
    ia4=IATournerAngleDroite(controleur,90,vitesse)
    iaseq=IAseq(controleur,[ia1,ia2,ia1,ia4,ia1,ia2,ia1])
    return iaseq
