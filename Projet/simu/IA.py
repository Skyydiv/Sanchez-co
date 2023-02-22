from objet import Robot
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
        self.robot.setVitesse(0, 0)
        self.parcouru_gauche = 0
        self.parcouru_droite = 0
        
        if self.parcouru_gauche > self.goal or self.parcouru_droite > self.goal:
            return True
        
        return False
    
    def update(self, delta_t):
            parcouru_g, parcouru_d = self.robot.get_distance_roue(delta_t)
            self.parcouru_gauche += parcouru_g
            self.parcouru_droite += parcouru_d
            if self.parcouru_gauche < self.goal and self.parcouru_droite < self.goal:
                self.robot.setVitesse(self.v, self.v)
            else:
                self.stop()
    
    
    
    
    
    
    
   
        
        
        
    