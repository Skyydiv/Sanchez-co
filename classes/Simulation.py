from Environnement import Environnement
from time import sleep
import random

class Simulation :
    """Simulation qui fait interagir le Robot avec son Environnement
    """
    
    def __init__(self, environnement:Environnement):
        '''Constructeur de la simulation qui initailise l'environnement et le robot 
        :param environnement: environnement dans lequel se déroule la simulation
        '''
        self.environnement=environnement
        self.robot=environnement.robot
        self.en_cours=False
        

    def simu(self):
        '''
        Gère la simulation, c'est à dire le temps, et les appels aux fonctions de déplacement du robot 
        '''
        while self.en_cours:
            self.update1pas()
            sleep(1/1000) #arrête l'execution chaque pas et rentre de nouveau dans la boucle (en gros fais la boucle  chaque 1 pas)

    def update1pas(self):
        nex_vdroite = round(random.uniform(self.robot.vitesseMin,self.robot.vitesseMax),1)
        nex_vgauche = round(random.uniform(self.robot.vitesseMin,self.robot.vitesseMax),1)
        self.robot.changerVitesse(nex_vgauche,nex_vdroite)
        self.robot.deplacer()
        
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
        i=0
        for i in range(nbObstacles) :
            newCoord=self.coordAlea()
            self.environnement.addObstacle(newCoord[0],newCoord[1],1,0,30)

    def start(self) : 
        '''Methode qui permet le lancement de la simulation'''
        self.en_cours=True
        try:
            self.simu()
        except Exception as e:
            self.en_cours=False
            print("Simulation failed with error:", e)

    def stop(self):
        '''Methode qui permet l'arrêt de la simulation'''
        self.en_cours=False


