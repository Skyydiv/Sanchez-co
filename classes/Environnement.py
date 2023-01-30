import numpy
from Robot import Robot
from Obstacle import Obstacle

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

    def verifieObstacle(self, x, y):
        '''Verfie s'il y a un obstacle dans la case x,y
        :param x: indice de la ligne
        :param y: indice de la colonne
        '''
        if (self.tab[int(x)][int(y)]==set()):
            return False
        elif self.tab[int(x)][int(y)]!=set(): 
            for i in self.tab[int(x)][int(y)]:
                if i.x==x and i.y==y:
                    return True
        return False
    
    def deposerRobot(self,robot):
        if self.tab[int(robot.x)][int(robot.y)]==set():
            self.tab[int(robot.x)][int(robot.y)].add(robot)
        elif self.tab[int(robot.x)][int(robot.y)]!=set():
            print("Il y a déjà un objet dans cette case veuillez changer les coordonnées du robot ou enlever les objets présents")

    def deposerObstable(self,x,y,h,d):
        i=True
        ob=Obstacle(x,y,h,d)
        if self.tab[int(x)][int(y)]==set():
            self.tab[int(x)][int(y)].add(ob)
        elif self.tab[int(x)][int(y)]!=set():
            if self.verifieObstacle(x,y):
                print("Il y a déjà un objet dans cette case veuillez changer les coordonnées dans les paramètres de la fonction")
            else:
                self.tab[int(x)][int(y)].add(ob)
    

    def deplacerRobot(self, robot):
        """
            Vérifie si il y a un obstacle aux coordonnés après le déplacement ou si il y a mur sur la route
                si oui on bouge pas
                sinon change les coordonnées x et y du robot
            :param robot: le robot à déplacer
        """
        new_x = robot.x + robot.vitesse[0]
        new_y = robot.y + robot.vitesse[1]
        if (self.verifieObstacle(new_x,new_y)) or (self.verifieMur(new_x,new_y)):
            return
        robot.x = new_x
        robot.y = new_y






                

#test 
env=Environnement(5,10,5)
rob=Robot([1.2,4])
ob1=Obstacle(1.2,3.4,4,5.6)
env.tab[int(ob1.x)][int(ob1.y)].add(ob1)
print(env.verifieObstacle(1.2,3.4))
env.deposerRobot(rob)
env.deposerObstable(1.2,3.5,4,5)



