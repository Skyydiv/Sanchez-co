import numpy
import random
from Objet import Robot
from Objet import Obstacle

class Environnement() :
    ''' L'environnement dans lequel se trouve le Robot'''

    def __init__(self,x,y,echelle):
        '''Constructeur de la classe Environnement, creer un tableau d'ensemble vide de x lignes et y colonnes
        
        :param x: nombre de lignes
        :param y: nombre de colonnes
        :param echelle: échelle 
        '''
        
        self.tab=numpy.empty([int(x),int(y)],dtype=set)  
        for i in range(int(x)):
            for j in range(int(y)):
                self.tab[i][j]=set()
        self.nblignes=int(x)
        self.nbcolonnes=int(y)
        self.echelle=echelle


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
<<<<<<< HEAD
                    print(' ')
            elif simu.environnement.tab[i][j]!=set():
                for obj in simu.environnement.tab[i][j]:
                    if isinstance(obj,Robot):
                        print('R')
                    elif isinstance(obj,Obstacle) :
                        print('O')
            print()
=======
                    print("*", end=" ")
                else:
                    for obj in simu.environnement.tab[i][j]:
                        if isinstance(obj,Robot):
                            print('R', end=" ")
                        elif isinstance(obj,Obstacle) :
                            print('O',end=" ")
            print()
        print("-------------")

>>>>>>> aa6744c70376b413d89795c24180dd456617dc20

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




#test 
# env=Environnement(5,10,5)
# rob=Robot([1.2,4])
# ob1=Obstacle(1.2,3.4,4,5.6)
# env.tab[int(ob1.x)][int(ob1.y)].add(ob1)
# print(env.verifieObstacle(1.2,3.4))
# env.addRobot(rob)
# env.addObstacle(1.2,3.5,4,5)
# env.deposer(3)



#test2
#env=Environnement(10,10,1)
#rob=Robot([2,0])
#rob.x=0.1
#rob.y=0.1
#env.addRobot(rob)
#print(env.tab[0][0]) #robot bien placé


#test estMur
#print("nblignes",env.nblignes)
#print("nbcolonnes",env.nbcolonnes)

#print("(3,3) ", env.estMur(3,3)) #ok
#print("(0,3) ", env.estMur(0,3)) #ok
#print("(0.1,3) ", env.estMur(0.1,3)) #ok

#print("(3,0) ", env.estMur(3,0)) #ok
#print("(3,10) ", env.estMur(3,10)) #ok
#print("(10,3) ", env.estMur(10,3)) #ok

#print("(10,10) ", env.estMur(10,10)) #ok
#print("(11,3) ", env.estMur(11,3)) #ok

#test deplacerRobot 
# print("position: ", robot1.x,robot1.y, "direction: ",robot1.vitesse)
# env1.deplacer(robot1)
# robot1.vitesse=[0,-3.4]
# print("position: ", robot1.x,robot1.y, "direction: ",robot1.vitesse)
# env1.deplacer(robot1)
# robot1.vitesse=[0,-3.4]
# print("position: ", robot1.x,robot1.y, "direction: ",robot1.vitesse)


