
import numpy
import random
import math
from Objet import Robot
from Objet import Obstacle

class Environnement() :
    ''' L'environnement dans lequel se trouve le Robot'''

    def __init__(self,coordsmax,robot,precision):
        '''Constructeur de la classe Environnement : avec des valeurs flottantes pour la taille de l'environnement. 
        L'environnement possede un ensemble d'obstacle qui contient tous les obstacles présents.
        
        :param coordsmax: coordsmax[0] représente la longueur et coordsmax[1] représente la largeur de l'espace (en cm)
        :param robot: le robot unique présent dans l'environnement
        :param precision: le plus petit écart entre 2 points pour les considérer distincts (en cm)
        '''
        self.coordsmax=coordsmax
        self.robot=robot
        self.precision=precision
        self.ensemble_obstacles= set()


    def estMur(self,x,y,rayon):
        '''
        Vérifie si les coordonée x et y sont dans l'enceinte de l'environnement. 
        :param x: coordonné réelle
        :param y: coordonné réelle
        :return False si on est dans l’environnement 
        :return True si on se prend un mur
        '''
        if ((x+rayon>=self.coordsmax[0]) or (y+rayon>=self.coordsmax[1]) or (x-rayon<=0) or (y-rayon<=0)):
            return True
        return False
    
    def estRobot(self,x, y,r):
        """Verifie si les coordonnées passées en parametre se trouve sur la surface du robot
        :param x: coordonnées en x
        :param y: coordonnées en y
        :param r:rayon en mm
        """
        if(self.robot.x+self.robot.rayon>=x-r and self.robot.x-self.robot.rayon<=x+r and self.robot.y+self.robot.rayon>=y-r and self.robot.y-self.robot.rayon<=y+r):
            return True

    def estObstacle(self, x, y,r):
        '''Verfie s'il y a un obstacle dans l'environnement avec les mêmes coordonnées
        :param x: coordonnées en x
        :param y: coordonnées en y
        :param r:rayon en mm
        :returns: True s'il existe déjà un obstacle avec les mêmes coordonnées, False sinon
        '''
        for i in self.ensemble_obstacles:
            if i.x+i.rayon>=x-r and i.x-i.rayon<=x+r and i.y+i.rayon>=y-r and i.y-i.rayon<=y+r:
                return True
        return False

    
    def addObstacle(self,x,y,h,d,rayon):
        """Créer et dépose l'obstacle s'il n'y a pas déjà un objet dans la case avec les mêmes coordonnées en faisant appel à la fonction estObstacle
        :param x: Coordonnées x de l'obstacle qu'on va créer
        :param y: Coordonnées y de l'obstacle qu'on va créer
        :param h: hauteur de l'obstacle
        :param d: distance du sol de l'obstacle
        """
        if not (self.estObstacle(x,y,rayon) and self.estMur(x,y,rayon) and self.estRobot):
            self.ensemble_obstacles.add(Obstacle(x,y,h,d,rayon))
        return

    def calculDistance(self, objet1, objet2):
        '''
        Calcule la distance entre deux objets passer en paramètre, en prenant compte le rayon le rayon des objets. Les objets peuvent être des robots ou des obstacles.
        :param objet1 : robot/obstacle
        :param objet2 : robot/obstacle
        :return : valeur négative ou égale à 0 si les objects sont en collision (ne gère pas la hauteur)
        :return : sinon valeur positive correspondant à la distance en valeur absolue la plus petite entre les 2 rayons (distance générale, ne pdonne pas la direction)
        '''

        return ( math.sqrt(math.pow(objet1.x-objet2.x,2)+ math.pow(objet1.y-objet2.y),2) - (objet1.rayon + objet2.rayon) )

    
    def detectCollision(self):
        '''
        verifie si les coordonnes du robot sont identiques a un obstacle de l’environnement ou s’il a pris un mur selon une precision
        '''
        return self.estObstacle(self.robot.x,self.robot.y,self.robot.rayon) or self.estMur(self.robot.x,self.robot.y,self.robot.rayon)
            
