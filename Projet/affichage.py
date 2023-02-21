from tkinter import *
from tkinter import ttk
from simu import *
#import simu (peut être remplacé par ça)

capteur = Capteur(0)
rob=Robot(30,capteur) # initialiser le robot
rob.setVitesse(100,80)
env=Environnement([1000,500],rob,5) # initialiser l'environment
simulation=Simulation(env,100)
simulation.addSimulation(5) #ajouter des obstcales a l'environnement
  
root = Tk() # initialiser la fenetre tkinter
view=View(root, simulation)
view.start_sim()
root.mainloop()
view.stop_sim()



