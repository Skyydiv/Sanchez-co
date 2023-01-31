from Environnement import Environnement
from Objet import Robot
from Objet import Obstacle
from time import sleep

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


    def simu(self):
        '''
        Gère la simulation, c'est à dire le temps, et les appels aux fonctions de déplacement du robot et d'affichage de la simulation
        '''
        date=0
        while date<self.temps:
            self.update()
            #appel d'affichage à changer si besoin et import view
            #view.action(self) #je donne la simulation en paramètre pour permettre de récupérer les attributs de la simulation
            date+=self.delta
            
            sleep(1) #attends 1 seconde

    def update(self):
        self.environnement.deplacer(self.robot)
        


