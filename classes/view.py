from tkinter import *

class View :
    '''L'interface graphique de la simulation'''
    def __init__(self,simu):
        '''Constructeur de l'interface graphique de la simulation
        :param simu: simulation qu'on veut représenter graphiquement
        '''
        self.simu=simu
        self.robot=simu.environnement.robot
        self.obstacles=simu.environnement.ensemble_obstacles
        self.longueur=simu.environnement.coordsmax[0]
        self.largeur=simu.environnement.coordsmax[1]