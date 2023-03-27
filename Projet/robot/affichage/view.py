from tkinter import *
from tkinter import ttk

from threading import Thread
from math import degrees



class View(Thread) :
    '''L'interface graphique de la simulation'''

    def __init__(self, master, simulation,delta_t):
        '''Constructeur de l'interface graphique de la simulation
        :param master: la fenetre de l'affichage
        :param simulation: simulation qu'on veut représenter graphiquement
        '''
        Thread.__init__(self)
    
        self.root=master

        self.sim=simulation
        self.delta=delta_t
        self.robot=simulation.robot
        self.obstacles=simulation.ensemble_obstacles
        self.longueur=simulation.coordsXmax
        self.largeur=simulation.coordsYmax


        self.canv=Canvas(self.root, bg="black",highlightbackground='white',highlightthickness=4, height=self.largeur, width=self.longueur)
        self.canv.pack()
        
        self.updateCanvas()

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
        o=degrees(self.robot.orientation)
        self.canv.create_arc(x-r,y-r,x+r,y+r, start=45-o, extent=270,fill="yellow")

    def drawObstacles(self):
        '''dessine l'ensemble des obstacles'''
        for obs in self.obstacles:
            x=obs.x
            y=obs.y
            r=obs.rayon
            self.canv.create_oval(x-r,y-r,x+r,y+r, fill='white')



