from Environnement import Environnement
from Objet import Robot
from Objet import Obstacle
import random

class Simulation :
    """Simulation qui fait interagir le Robot avec son Environnement
    """
    
    def __init__(self, temps, pas,robot,environnement):
        '''Constructeur de la simulation qui initailise l'environnement,le robot, le temps de la simulation et le pas de temps
        :param temps: temps de la simulation
        :param pas: pas de temps
        :param x: nblignes pour environnement
        :param y: nbcolonnes pour environnement
        :param echelle: l'échelle pour environnement
        :param vitesse: vitesse du robot'''
        self.environnement=environnement
        self.robot=robot
        self.temps=temps
        self.delta=pas

    def coordAlea(self) :
        '''Renvoie des coord aléatoires x et y non occupés dans l'environnement'''
        x=round(random.uniform(0,self.environnement.nblignes),1)
        y=round(random.uniform(0,self.environnement.nbcolonnes),1)
        if(self.environnement.estObstacle(x,y)  or self.environnement.estMur(x,y) or (self.robot.x==x and self.robot.y==y)):
            return self.coordAlea()  
        else:
            return (x,y)
            

    def addSimulation(self,nbObstacles):
        '''Depose le robot et nbObstacles obstacles dans des positions aléatoires dans l'environnement
        :param nbObstacles: nombre d'obstacles a déposer
        '''
        self.environnement.addRobot(self.robot)
        i=0
        for i in range(nbObstacles) :
            newCoord=self.coordAlea
            self.environnement.addObstacle(newCoord[0],newCoord[1],1,0)

#tests de Haya

env2=Environnement(10,10,1)
robot2=Robot([2,2])

simu=Simulation(10,1,robot2,env2)

#test de addSimulation
simu.addSimulation(10)