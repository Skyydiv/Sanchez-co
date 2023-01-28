from Environnement import Environnement
from Robot import Robot
from Obstacle import Obstacle

class Simulation :
    '''Simulation qui fait interagir le Robot et son Environnement'''
    
    def __init__(self, temps, pas):
        '''Constructeur de la simulation qui initailise l'environnement,le robot, le temps de la simulation et le pas de temps
        :param temps: temps de la simulation
        :param pas: pas de temps'''
        self.environnement=Environnement()
        self.robot=Robot()
        self.temps=temps
        self.delta=pas