from time import sleep
import random
from threading import Thread
from simu import Environnement
from IA import Ia_Avancer_tout_droit, IAseq, IAangle, Ia, IAevitecrash


class Simulation :
    """Simulation qui fait interagir le Robot avec son Environnement
    """
    
    def __init__(self, environnement:Environnement, delta_t):
        '''Constructeur de la simulation qui initailise l'environnement et le robot 
        :param environnement: environnement dans lequel se déroule la simulation
        '''
        self.environnement=environnement
        self.robot=environnement.robot
        self.delta_t=delta_t
        self.en_cours=False

    def run_simu(self):
        """lance la simulation"""
        self.en_cours=True
        threadSimu=Thread(target=self.boucle)
        threadSimu.start()

    def boucle(self):
        '''
        La boucle qui avance la simulation chaque pas de temps
        '''
        while self.en_cours:
            self.update1pas()
            sleep(1./self.delta_t) #arrête l'execution chaque pas et rentre de nouveau dans la boucle (en gros fais la boucle  chaque 1 pas)


    def update1pas(self):
        #IA.Ia_Avancer_tout_droit(self.robot,0.1,150).update(1/self.delta_t)
        self.robot.deplacer(1./self.delta_t)
        if(self.environnement.detectCollision()):
            self.stop_simu()


    def coordAlea(self) :
        '''Renvoie des coord aléatoires x et y non occupés dans l'environnement'''
        x=round(random.uniform(0,self.environnement.coordsmax[0]-1),1)
        y=round(random.uniform(0,self.environnement.coordsmax[1]-1),1)
        if(self.environnement.estObstacle(x,y,31)  or self.environnement.estMur(x,y,31) or (self.robot.x==x and self.robot.y==y)):
            return self.coordAlea()  
        else:
            return (x,y)
            

    def addSimulation(self,nbObstacles):
        '''Depose nbObstacles obstacles dans des positions aléatoires dans l'environnement
        :param nbObstacles: nombre d'obstacles a déposer
        '''
        for i in range(nbObstacles) :
            newCoord=self.coordAlea()
            self.environnement.addObstacle(newCoord[0],newCoord[1],1,0,30)

    def stop_simu(self):
        '''Methode qui permet l'arrêt de la simulation'''
        self.en_cours=False


    


