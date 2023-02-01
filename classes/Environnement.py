import numpy
<<<<<<< HEAD
from Robot import Robot

=======
import random
from Objet import Robot
from Objet import Obstacle
>>>>>>> f5f8ffabb1c629a7d445fcc1e63b8aad8b7c8b7e

class Environnement() :
    ''' L'environnement dans lequel se trouve le Robot'''

    def __init__(self,x,y,echelle):
        '''Constructeur de la classe Environnement, creer un tableau d'ensemble vide de x lignes et y colonnes
        
        :param x: nombre de lignes
        :param y: nombre de colonnes
        :param echelle: échelle 
        '''
<<<<<<< HEAD
        self.tab=numpy.empty((int(x),int(y)),set())
        for i in range(x):
            for j in range(y):
                self.tab[i][j]=numpy.empty(set())
=======
        
        self.tab=numpy.empty([int(x),int(y)],dtype=set)  
        for i in range(int(x)):
            for j in range(int(y)):
                self.tab[i][j]=set()
>>>>>>> f5f8ffabb1c629a7d445fcc1e63b8aad8b7c8b7e
        self.nblignes=int(x)
        self.nbcolonnes=int(y)
        self.echelle=echelle


<<<<<<< HEAD
    def VerifieMur(self,a,env):
        '''Verfie si quand le robot avance de a il y a un mur
        :param a: le nombre de case que va parcourir le robot 
        '''
        if ((self.orientation=="droite")and((self.y+a)>=env.nbcolonnes)):
            return False
        elif ((self.orientation=="gauche")and((self.y-a)<0)):
            return False
        elif ((self.orientation=="haut")and((self.x-a)<0)):
            return False
        elif ((self.orientation=="bas")and((self.x+a)>=env.nblignes)):
            return False
        else:
            return True
=======
    def estMur(self,x,y):
        '''
        Vérifie si les coordonée x et y sont dans l'enceinte de l'environnement. 
        :param x: coordonné réelle
        :param y: coordonné réelle
        :return False si on est dans l’environnement 
        :return True si on se prend un mur
        '''
        if ((x>=self.nblignes) or (y>=self.nbcolonnes) or (x<=0) or (y<=0)):
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
    
    def addRobot(self,robot):
        """ Dépose le robot en paramètre s'il y a aucun obstacle dans la case où on veut le poser.
        :param robot: robot à déposer 
        """
        if not (self.estObstacle(robot.x,robot.y) and self.estMur(robot.x,robot.y)):
            self.tab[int(robot.x)][int(robot.y)].add(robot)
        return 
        

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


    def changementVitesse(self,robot,vx,vy):
        """
         change le vecteur de vitesse du robot 
         :param vx: vitesse vx
         :param vy: vitesse vy
        """
        robot.vitesse[0]=vx
        robot.vitesse[1]=vy


    def distToCase(self,echelle,x, y) :
        """
        renvoie la distance du robot dans la case en considérant l'échelle
        :param echelle: echelle de l'environnement
        :param x: abscisse de l'objet
        :param y: ordonnée de l'objet
        """
        return (x*echelle,y*echelle)


    def afficher(simu):
        """
        Affiche l'environnemment en mettant 'R' s'il y a un robot, 'O' s'il y a un obstacle et ' ' si rien.
        """
        for i in range (simu.environnement.nblignes):
            for j in range (simu.environnement.nbcolonnes):
                if simu.environnement.tab[i][j]==set():
                    print("*", end=" ")
                else:
                    for obj in simu.environnement.tab[i][j]:
                        if isinstance(obj,Robot):
                            print('R', end=" ")
                        elif isinstance(obj,Obstacle) :
                            print('O',end=" ")
            print()
        print("-------------")


#tests de Haya

env1=Environnement(10,5,10)
robot1=Robot([6,4])

#test estMur
assert(env1.estMur(2,-1)==True)

#test addObstacle
env1.addObstacle(4.14,3.6,1,0)
assert(env1.tab[4][3]!=set())

#test estObstacle
assert(env1.estObstacle(4.14,3.6)==True)

#test addRobot
env1.addRobot(robot1)
assert(robot1 in env1.tab[0][0])

#test deplacer
env1.deplacer(robot1)
assert(robot1.x==6.1 and robot1.y==4.1)

#test distToCase
# print(env1.distToCase(env1.echelle,robot1.x,robot1.y))

>>>>>>> f5f8ffabb1c629a7d445fcc1e63b8aad8b7c8b7e




<<<<<<< HEAD
         
=======
>>>>>>> f5f8ffabb1c629a7d445fcc1e63b8aad8b7c8b7e

