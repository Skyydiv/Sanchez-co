from tkinter import *
from tkinter import ttk

class View :
    '''L'interface graphique de la simulation'''

    def __init__(self,simu):
        '''Constructeur de l'interface graphique de la simulation
        :param simu: simulation qu'on veut représenter graphiquement
        '''
        self.root=Tk()
        self.root.title("Simulation de Dexter")

        self.simu=simu
        self.robot=simu.environnement.robot
        self.obstacles=simu.environnement.ensemble_obstacles
        self.longueur=simu.environnement.coordsmax[0]
        self.largeur=simu.environnement.coordsmax[1]

        #create canva
        self.can=Canvas(self.root, bg="black",highlightbackground='white',highlightthickness=4, height=self.largeur, width=self.longueur)

        #draw robot
        can.create_arc(self.robot.x,self.robot.y,self.robot.rayon, self.robot.rayon, start=45, extent=270,fill="yellow")