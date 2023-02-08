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
        if(self.robot.x+self.robot.rayon>=x-r and self.robot.x-self.robot.rayon<=x+r and self.robot.y+self.robot.rayon>=y-r and self.robot.y-self.robot.rayon<=y+r):
            return True

    def estObstacle(self, x, y,r):
        '''Verfie s'il y a un obstacle dans l'environnement avec les mêmes coordonnées
        :param x: indice de la ligne
        :param y: indice de la colonne
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
<<<<<<< HEAD
<<<<<<< HEAD
        return ((abs(objet1.x-objet2.x) + abs(objet1.y-objet2.y)) - (objet1.rayon + objet2.rayon))
=======
        return ( (abs(objet1.x-objet2.x) + abs(objet1.y-objet2.y)) - (objet1.rayon + objet2.rayon) )
=======

        return ((abs(objet1.x-objet2.x) + abs(objet1.y-objet2.y)) - (objet1.rayon + objet2.rayon))
<<<<<<< HEAD
        
>>>>>>> f1e1920a0a456af9bbb91ce138fbf1f5d78df641
=======

>>>>>>> dbfd0c13210b359038929c493ecc6fb28dfdfc0f
    
    def detectCollision(self):
        '''
        verifie si les coordonnes du robot sont identiques a un obstacle de l’environnement ou s’il a pris un mur selon une precision
        '''
<<<<<<< HEAD
        if self.estObstacle(Robot.x,Robot.y) or self.estMur(Robot.x,Robot.y):
<<<<<<< HEAD
            return " Collision detectée"
        
        
>>>>>>> 590e454113df826660f053194898b6ffc949aa2a

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


=======
            return " Collision detectée"
>>>>>>> f1e1920a0a456af9bbb91ce138fbf1f5d78df641
=======
        return self.estObstacle(self.robot.x,self.robot.y,self.robot.rayon) or self.estMur(self.robot.x,self.robot.y,self.robot.rayon)
            
>>>>>>> dbfd0c13210b359038929c493ecc6fb28dfdfc0f
