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
    
    def deposerRobot(self,robot):
        """ Dépose le root en paramètre s'il y a aucun obstacle dans la case où on veut le poser.
        :param robot: robot à déposer """
        if self.tab[int(robot.x)][int(robot.y)]==set():
            self.tab[int(robot.x)][int(robot.y)].add(robot)
        elif self.tab[int(robot.x)][int(robot.y)]!=set():
            print("Il y a déjà un objet dans cette case veuillez changer les coordonnées du robot ou enlever les objets présents")

    def deposerObstable(self,x,y,h,d):
        """ Dépose les obstacles s'il n'y a pas déjà un objet dans la case avec les mêmes coordonnées en faisant appel à la fonction verifieObstacle
        :param x: Coordonnées x de l'obstacle qu'on va créer*
        :param y: Coordonnées y de l'obstacle qu'on va créer
        :param h: hauteur de l'obstacle
        :param d: distance du sol de l'obstacle
        """
        
        i=True
        ob=Obstacle(x,y,h,d)
        if self.tab[int(x)][int(y)]==set():
            self.tab[int(x)][int(y)].add(ob)
        elif self.tab[int(x)][int(y)]!=set():
            if self.verifieObstacle(x,y):
                print("Il y a déjà un objet dans cette case veuillez changer les coordonnées dans les paramètres de la fonction")
            else:
                self.tab[int(x)][int(y)].add(ob)






                

#test 
env=Environnement(5,10,5)
rob=Robot([1.2,4])
ob1=Obstacle(1.2,3.4,4,5.6)
env.tab[int(ob1.x)][int(ob1.y)].add(ob1)
print(env.verifieObstacle(1.2,3.4))
env.deposerRobot(rob)
env.deposerObstable(1.2,3.5,4,5)



