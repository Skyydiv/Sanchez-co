from tkinter import *
from tkinter import ttk
from simu import Robot, Environnement, Simulation, Capteur
from affichage import View

capteur = Capteur(0)
rob=Robot(Robot.WHEEL_BASE_WIDTH/2,capteur) # initialiser le robot
rob.setVitesse(100,80)
env=Environnement([1500,800],rob,5) # initialiser l'environment
simulation=Simulation(env,100)
simulation.addSimulation(5) #ajouter des obstcales a l'environnement


  
root = Tk() # initialiser la fenetre tkinter
view=View(root, simulation)
simulation.run_simu()
# view.start_sim()
root.mainloop()
simulation.stop_simu()
# view.stop_sim()



