from tkinter import *
from tkinter import ttk
from robot.simu.objet import Robot, Environnement
from robot.affichage import View
from robot.simu.simulation import Simulation
from robot.IA import Ia_Avancer_tout_droit
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


simulation=Simulation(100)
simulation.addSimulation(5) #ajouter des obstcales a l'environnement

ia=Ia_Avancer_tout_droit(simulation.robot,100,60)
ia.start()
  

root = Tk() # initialiser la fenetre tkinter
view=View(root, simulation)
simulation.run_simu()
# view.start_sim()
root.mainloop()
simulation.stop_simu()
# view.stop_sim()



