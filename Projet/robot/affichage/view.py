from tkinter import *
from tkinter import ttk

from threading import Thread
from math import degrees
import math
import random


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

        self.robot_trajet=[]

        self.canv=Canvas(self.root, bg="black",highlightbackground='white',highlightthickness=4, height=self.largeur, width=self.longueur)
        self.canv.pack()
        
        self.updateCanvas()

    def updateCanvas(self):
        '''Initialise la canvas a chaque pas'''
        self.canv.delete("all") 
        self.drawRobot()
        self.drawObstacles()
        self.drawRobotTrajet()
        self.root.after(self.delta,self.updateCanvas)
        
    
    def drawRobot(self):
        '''dessine le Robot'''
        x=self.robot.x
        y=self.robot.y
        r=self.robot.rayon
        o=degrees(self.robot.orientation)
        self.canv.create_arc(x-r,y-r,x+r,y+r, start=45-o, extent=270,fill="#FD6C9E")

        self.robot_trajet.append((x, y))
        #création de 2 leds devant le robot selon son orientation (un a gauche et un à droite)
        if (self.robot.led1==False and self.robot.led2==False):
            color1='white'
            color2='white'
        elif (self.robot.led1==True and self.robot.led2==False):
            color1='red'
            color2='white'
        elif (self.robot.led1==False and self.robot.led2==True):
            color1='white'
            color2='blue' 
        else:
            color1='red'
            color2='blue'
        self.canv.create_oval(x+r*math.cos(math.radians(o+45)),y+r*math.sin(math.radians(o+45)),x+r*math.cos(math.radians(o+45))+10,y+r*math.sin(math.radians(o+45))+10, fill=color1)
        self.canv.create_oval(x+r*math.cos(math.radians(o-45)),y+r*math.sin(math.radians(o-45)),x+r*math.cos(math.radians(o-45))+10,y+r*math.sin(math.radians(o-45))+10, fill=color2)


        
    def drawRobotTrajet(self):
        '''dessine le trajet du robot'''
        if len(self.robot_trajet) > 1:
            self.canv.create_line(self.robot_trajet, fill='white')

    def drawObstacles(self):
        '''dessine l'ensemble des obstacles'''
        for obs in self.obstacles:
            x=obs.x
            y=obs.y
            r=obs.rayon
            self.canv.create_oval(x-r,y-r,x+r,y+r, fill='white')



