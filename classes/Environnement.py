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

    def afficheTab(self):
        '''Affiche l'environnement dans la console'''
        for ligne in self.tab:
            for elt in ligne:
                if isinstance(elt,Robot):
                    print("Robot", end=", ")
                else :
                    print(elt, end=", ")
            print()