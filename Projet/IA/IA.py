from simu import *
from abc import ABC, abstractmethod
import math

class Ia(ABC):
    @abstractmethod
    def start(self):
        pass

    
    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def update(self):
        pass


class Ia_Avancer_tout_droit(Ia):
    
    def __init__(self, robot, distance, v):
        self.robot = robot
        self.parcouru_gauche = 0
        self.parcouru_droite = 0
        self.goal = distance
        self.v = v
    
    def start(self):
        self.parcouru_gauche = 0
        self.parcouru_droite = 0
            
    def stop(self):
        # Si l'une des roues a parcouru plus que la distance à parcourir, arrêter le robot
        if self.parcouru_gauche > self.goal and self.parcouru_droite > self.goal:
            return True
        return False
    
    def update(self, delta_t):
            if self.stop():
                self.robot.setVitesse(0, 0)
                self.parcouru_gauche = 0
                self.parcouru_droite = 0
            else:
                parcouru_g, parcouru_d = self.robot.get_distance_roue(delta_t)
                if self.parcouru_gauche < self.goal or self.parcouru_droite < self.goal:
                    self.robot.setVitesse(self.v, self.v)
                    self.robot.deplacer(delta_t)
                    self.parcouru_gauche += parcouru_g
                    self.parcouru_droite += parcouru_d

    
class IAangle(Ia):
    """
    sous-classe de l'IA permettant permettant une rotation du robot d'un angle donné 
    """
    def __init__(self, robot, angle):
        
        self.robot = robot
        self.running = False
        self.angle = angle
        
        

    def start(self):
        if not self.running:
            self.running = True
            
        


    def stop(self):
        return self.robot.orientation == self.angle
    

    def update(self, delta_t):
        if self.running:
            if self.stop(): 
                return
            else:
                self.robot.orientation = self.angle
    
    
    
class IAseq(Ia):
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
    


class IAevitecrash(Ia):
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
   
        
        
        
    
