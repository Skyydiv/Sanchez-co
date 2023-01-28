import numpy
from Robot import Robot


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
                self.tab[i][j]={None}
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

#test 
env=Environnement(5,10,5)
rob=Robot([2,3])
env.tab[0][0].add(rob)
if rob in env.tab[0][0]:
    print('R')


