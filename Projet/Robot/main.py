from tkinter import *
from tkinter import ttk
from module.simu.objet import Robot, Environnement
from module.affichage import View
from module.simu.simulation import Simulation
from module.IA import Ia_Avancer_tout_droit


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



