from tkinter import *
from tkinter import ttk
from Simulation import Simulation
from Objet import Robot
from Environnement import Environnement

class View :
    '''L'interface graphique de la simulation'''

    def __init__(self, master, simulation):
        '''Constructeur de l'interface graphique de la simulation
        :param master: la fenetre de l'affichage
        :param simulation: simulation qu'on veut représenter graphiquement
        '''
    
        self.root=master

        self.sim=simulation
        self.delta=simulation.delta_t
        self.robot=simulation.environnement.robot
        self.obstacles=simulation.environnement.ensemble_obstacles
        self.longueur=simulation.environnement.coordsmax[0]
        self.largeur=simulation.environnement.coordsmax[1]


        self.canv=Canvas(self.root, bg="black",highlightbackground='white',highlightthickness=4, height=self.largeur, width=self.longueur)
        self.canv.pack()

        # self.Start_Stop_button=Button(self.root, text="Start/Stop", command=self.toggle)
        # self.Start_Stop_button.pack()
        
        self.updateCanvas()

        
    # def toggle(self):
    #     '''Lance ou arrête l'éxécution selon l'état de la simulation avec le click sur le boutton'''
    #     if self.sim.en_cours:
    #         self.start_sim()
    #     else:
    #          self.stop_sim()

    def updateCanvas(self):
        '''Initialise la canvas a chaque pas'''
        self.canv.delete("all") 
        self.drawRobot()
        self.drawObstacles()
        self.root.after(self.delta,self.updateCanvas)
        
    
    def drawRobot(self):
        '''dessine le Robot'''
        x=self.robot.x
        y=self.robot.y
        r=self.robot.rayon
        self.canv.create_arc(x-r,y-r,x+r,y+r, start=45, extent=270,fill="yellow")

    def drawObstacles(self):
        '''dessine l'ensemble des obstacles'''
        for obs in self.obstacles:
            x=obs.x
            y=obs.y
            r=obs.rayon
            self.canv.create_oval(x-r,y-r,x+r,y+r, fill='white')

    def start_sim(self):
        self.sim.run_simu()

    def stop_sim(self):
        self.sim.stop_simu()


