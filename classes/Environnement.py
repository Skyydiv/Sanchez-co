import numpy
import random
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


    def estMur(self,x,y):
        '''
        Vérifie si les coordonée x et y sont dans l'enceinte de l'environnement. 
        :param x: coordonné réelle
        :param y: coordonné réelle
        :return False si on est dans l’environnement 
        :return True si on se prend un mur
        '''
        if ((x>=self.coordsmax[0]) or (y>=self.coordsmax[1]) or (x<=0) or (y<=0)):
            return True
        return False

    def estObstacle(self, x, y):
        '''Verfie s'il y a un obstacle dans la case avec les mêmes coordonnées
        :param x: indice de la ligne
        :param y: indice de la colonne
        :returns: True s'il existe déjà un obstacle avec les mêmes coordonnées, False sinon
        '''
        if (self.tab[int(x)][int(y)]==set()):
            return False
        elif self.tab[int(x)][int(y)]!=set(): 
            for i in self.tab[int(x)][int(y)]:
                if i.x==x and i.y==y:
                    return True
        return False
        
    def addObstacle(self,x,y,h,d):
        """Créer et dépose l'obstacle s'il n'y a pas déjà un objet dans la case avec les mêmes coordonnées en faisant appel à la fonction estObstacle
        :param x: Coordonnées x de l'obstacle qu'on va créer
        :param y: Coordonnées y de l'obstacle qu'on va créer
        :param h: hauteur de l'obstacle
        :param d: distance du sol de l'obstacle
        """
        if not (self.estObstacle(x,y) and self.estMur(x,y)):
            self.tab[int(x)][int(y)].add(Obstacle(x,y,h,d))
        return
    


    def deplacer(self,robot):
        """
        Vérifie si il y a un obstacle aux coordonnés après le déplacement ou si il y a mur sur la route
        si oui on bouge pas
        sinon change les coordonnées x et y du robot
        :param robot: le robot à déplacer
        """
        new_x = robot.x + robot.vitesse[0]
        new_y = robot.y + robot.vitesse[1]
        if not (self.estObstacle(new_x,new_y) and self.estMur(new_x,new_y)):
            self.tab[int(robot.x)][int(robot.y)].remove(robot)
            robot.x = new_x
            robot.y = new_y
            self.tab[int(robot.x)][int(robot.y)].add(robot)
        return



#tests de Haya

#env1=Environnement(10,5,10)
#robot1=Robot([6,4])

#test estMur
#assert(env1.estMur(2,-1)==True)

#test addObstacle
#env1.addObstacle(4.14,3.6,1,0)
#assert(env1.tab[4][3]!=set())

#test estObstacle
#assert(env1.estObstacle(4.14,3.6)==True)

#test addRobot
#env1.addRobot(robot1)
#assert(robot1 in env1.tab[0][0])

#test deplacer
#env1.deplacer(robot1)
#assert(robot1.x==6.1 and robot1.y==4.1)

#test distToCase
# print(env1.distToCase(env1.echelle,robot1.x,robot1.y))


