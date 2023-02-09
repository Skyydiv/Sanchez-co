from tkinter import *
from tkinter import ttk
from Simulation import Simulation
from view import View 
from Objet import Robot
from Environnement import Environnement

rob=Robot(4,4,30) # initialiser le robot
env=Environnement([1000,500],rob,5) # initialiser l'environment
simulation = Simulation(10000,env)
simulation.addSimulation(5) #ajouter des obstcales a l'environnement

#simulation.start() #lancer la simulation
    
root = Tk() # initialiser la fenetre tkinter
View(root, simulation)
root.mainloop()

#simulation.stop()