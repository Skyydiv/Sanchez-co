from Environnement import Environnement
from time import sleep
import random

class Simulation :
    """Simulation qui fait interagir le Robot avec son Environnement
    """
    
    def __init__(self, pas, environnement:Environnement):
        '''Constructeur de la simulation qui initailise l'environnement,l e robot et le pas de temps
        :param pas: pas de temps en millieseconde
        :param environnement: environnement dans lequel se déroule la simulation
        '''
        self.environnement=environnement
        self.robot=environnement.robot
        self.delta=pas
        self.en_cours=False
        

    def simu(self):
        '''
        Gère la simulation, c'est à dire le temps, et les appels aux fonctions de déplacement du robot 
        '''
        while self.en_cours:
            self.update1pas()
            #view.action(self) #je donne la simulation en paramètre pour permettre de récupérer les attributs de la simulation
            sleep(self.delta) #arrête l'execution chaque pas et rentre de nouveau dans la boucle (en gros fais la boucle  chaque 1 pas)

    def update1pas(self):
        nex_vx = round(random.uniform(0,2),1)
        nex_vy = round(random.uniform(0,2),1)
        self.environnement.changementVitesse(self.robot,nex_vx,nex_vy)
        self.environnement.deplacer(self.robot)
        
        
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
            newCoord=self.coordAlea()
            self.environnement.addObstacle(newCoord[0],newCoord[1],1,0)

    def start(self) : 
        '''Methode qui permet le lancement de la simulation'''
        self.en_cours=True
        self.simu()

    def stop(self):
        '''Methode qui permet l'arrêt de la simulation'''
        self.en_cours=False

#tests de Haya

# env2=Environnement(10,10,1)
# robot2=Robot([2,2])

# simul=Simulation(10,1,robot2,env2)

#test de addSimulation

# simul.addSimulation(10)
# assert(simu.robot in simu.environnement.tab[0][0]) 
# print(round(random.uniform(0,2),1))


# simul.addSimulation(10)
# assert(simu.robot in simu.environnement.tab[0][0]) 
# print(round(random.uniform(0,2),1))
