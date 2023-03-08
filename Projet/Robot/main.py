from tkinter import *
from tkinter import ttk
from module.simu.objet import Robot, Environnement
from module.simu.capteur import Capteur
from module.affichage import View
from module.simu.simulation import Simulation
from module.IA import Ia_Avancer_tout_droit


capteur = Capteur(0)
rob=Robot(Robot.WHEEL_BASE_WIDTH/2,capteur) # initialiser le robot

env=Environnement([1500,800],rob,5) # initialiser l'environment
simulation=Simulation(env,100)
simulation.addSimulation(5) #ajouter des obstcales a l'environnement

ia=Ia_Avancer_tout_droit(rob,100,60)

ia.start()
  
root = Tk() # initialiser la fenetre tkinter
view=View(root, simulation)
simulation.run_simu()
# view.start_sim()
root.mainloop()
simulation.stop_simu()
# view.stop_sim()



