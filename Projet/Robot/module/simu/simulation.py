from time import sleep
import random
from threading import Thread

class Simulation :
    """Simulation qui fait interagir le Robot avec son Environnement
    """
    
    def __init__(self, environnement, delta_t):
        '''Constructeur de la simulation qui initailise l'environnement et le robot 
        :param environnement: environnement dans lequel se déroule la simulation
        '''
        self._environnement=environnement
        self._robot=environnement.robot
        self._delta_t=delta_t
        self.en_cours=False
    
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
    

    def run_simu(self):
        """lance la simulation"""
        self._en_cours=True
        threadSimu=Thread(target=self.boucle)
        threadSimu.start()

    def boucle(self):
        '''
        La boucle qui avance la simulation chaque pas de temps
        '''
        while self._en_cours:
            self.update1pas()
            sleep(1./self._delta_t) #arrête l'execution chaque pas et rentre de nouveau dans la boucle (en gros fais la boucle  chaque 1 pas)


    def update1pas(self):
        #IA.Ia_Avancer_tout_droit(self.robot,0.1,150).update(1/self.delta_t)
        self._robot.deplacer(1./self._delta_t)
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
            

    def addSimulation(self,nbObstacles):
        '''Depose nbObstacles obstacles dans des positions aléatoires dans l'environnement
        :param nbObstacles: nombre d'obstacles a déposer
        '''
        for i in range(nbObstacles) :
            newCoord=self.coordAlea()
            self._environnement.addObstacle(newCoord[0],newCoord[1],1,0,30)

    def stop_simu(self):
        '''Methode qui permet l'arrêt de la simulation'''
        self._en_cours=False


    


