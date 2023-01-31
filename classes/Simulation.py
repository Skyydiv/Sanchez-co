from Environnement import Environnement
from Objet import Robot
from Objet import Obstacle

class Simulation :
    '''Simulation qui fait interagir le Robot avec son Environnement'''
    
    def __init__(self, temps, pas):
        '''Constructeur de la simulation qui initailise l'environnement,le robot, le temps de la simulation et le pas de temps
        :param temps: temps de la simulation
        :param pas: pas de temps'''
        self.environnement=Environnement()
        self.robot=Robot()
        self.temps=temps
        self.delta=pas