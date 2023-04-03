from time import sleep
import random
from threading import Thread
from .virtuel import Environnement
from .virtuel import Robot 
from time import time

class Simulation :
    """Simulation qui fait interagir le Robot avec son Environnement
    """
    
    SIMU_WIDTH=1500
    SIMU_HEIGHT=800
    SIMU_PRECESION=20

    def __init__(self,delta_t,x,y,b):
        '''Constructeur de la simulation qui initailise l'environnement et le robot 
        :param environnement: environnement dans lequel se déroule la simulation
        '''
        self._robot=Robot(Robot.WHEEL_BASE_WIDTH/2,x,y) # initialiser le robot        
        self._environnement=Environnement([Simulation.SIMU_WIDTH,Simulation.SIMU_HEIGHT],self._robot,Simulation.SIMU_PRECESION) # initialiser l'environment
        self._delta_t=delta_t
        self.en_cours=False
        self.deb=0
        self.fin=0
        self.temps_total=0
        self.crayon=self._robot.dessine(b)
    
    @property
    def environnement(self):
        """Renvoie l'environnement de la simulation"""
        return self._environnement
    
    @property
    def delta_t(self):
        """Renvoie le delta_t de la simulation"""
        return self._delta_t
      
    @property
    def coordsXmax(self):
      """Renvoie les coordonnées x de l'environnement """
      return self._environnement.coordsXmax
    
    @property
    def coordsYmax(self):
      """Renvoie les coordonnées y de l'environnement"""
      return self._environnement.coordsYmax
    
    @property
    def ensemble_obstacles(self):
       """Renvoie l'ensemble des obstacles de l'environnement"""
       return self._environnement.ensemble_obstacles
    
    @property
    def robot(self):
      """Renvoie le robot de la simulation"""
      return self._robot
        
    @property
    def robotX(self):
       """Renvoie les coordonnées x du robot"""
       return self._environnement.robotX
    
    @property
    def robotY(self):
       """Renvoie les coordonnées y du robot """
       return self._environnement.robotY
    
    @property
    def robotRayon(self):
        """Renvoie le rayon du robot """
        return self._environnement.robotRayon
    
    def reset_time(self):
        self.deb=time()
        self.temps_total=0
    
    def run_simu(self):
        """lance la simulation"""
        self._en_cours=True
        threadSimu=Thread(target=self.boucle)
        threadSimu.start()

    def boucle(self):
        '''
        La boucle qui avance la simulation chaque pas de temps
        '''
        self.reset_time()
        while self._en_cours:
            self.update1pas()
            sleep(1./self._delta_t) #arrête l'execution chaque pas et rentre de nouveau dans la boucle (en gros fais la boucle  chaque 1 pas)


    def update1pas(self): 
        self.fin=time()
        self.temps_total=self.fin-self.deb
        self.deb=self.fin
        self._robot.deplacer(self.temps_total)
        if(self._environnement.detectCollision()):
            self.stop_simu()


    def coordAlea(self) :
        '''Renvoie des coord aléatoires x et y non occupés dans l'environnement'''
        x=round(random.uniform(0,self.coordsXmax-1),1)
        y=round(random.uniform(0,self.coordsYmax-1),1)
        if(self._environnement.estObstacle(x,y,31)  or self._environnement.estMur(x,y,31) or (self.robotX==x and self.robotY==y)):
            return self.coordAlea()  
        else:
            return (x,y)
        
    def addSimulation(self):
        '''Depose nbObstacles obstacles dans des positions aléatoires dans l'environnement
        :param nbObstacles: nombre d'obstacles a déposer
        '''
        # for i in range(nbObstacles) :
        #     newCoord=self.coordAlea()
        #     self._environnement.addObstacle(newCoord[0],newCoord[1],1,0,30)

        self._environnement.addObstacle(60,60,1,0,30)
        self._environnement.addObstacle(1500-60,60,1,0,30)
        self._environnement.addObstacle(60,800-60,1,0,30)
        self._environnement.addObstacle(1500-60,800-60,1,0,30)

    def stop_simu(self):
        '''Methode qui permet l'arrêt de la simulation'''
        self._en_cours=False


    


