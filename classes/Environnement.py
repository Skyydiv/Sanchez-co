import numpy
from Objet import Robot


class Environnement() :
    ''' L'environnement dans lequel se trouve le Robot'''

    def __init__(self,x,y):
        '''Constructeur de la classe Environnement, creer un tableau vide de robot de x lignes et y colonnes
        
        :param x: nombre de lignes
        :param y: nombre de colonnes
        '''
        self.tab=numpy.empty((int(x),int(y)),Robot)
        self.nblignes=int(x)
        self.nbcolonnes=int(y)

    def VerifieMur(self,a,env):
        '''Verfie si quand le robot avance de a il y a un mur
        :param a: le nombre de case que va parcourir le robot 
        '''
        if ((self.orientation=="droite")and((self.y+a)>=env.nbcolonnes)):
            print("Attention il y a un mur!!")
            return True
        elif ((self.orientation=="gauche")and((self.y-a)<0)):
            print("Attention il y a un mur!!")
            return True
        elif ((self.orientation=="haut")and((self.x-a)<0)):
            print("Attention il y a un mur!!")
            return True
        elif ((self.orientation=="bas")and((self.x+a)>=env.nblignes)):
            print("Attention il y a un mur!!")
            return True
        else:
            print("Le robot peut avancer")
            return False




         

