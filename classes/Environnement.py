import numpy
from Robot import Robot

class Environnement() :
    ''' L'environnement dans lequel se trouve le Robot'''

    def __init__(self,n):
        '''Constructeur de la classe Environnement, creer un tableau vide de robot de dimension nxn
        
        :param n: dimension du tableau
        '''
        self.tab=numpy.empty((n,n),Robot)
        self.taille=n




    

