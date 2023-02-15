from tkinter import *
from tkinter import ttk
from Simulation import Simulation
from view import View 
from Objet import Robot
from Environnement import Environnement

rob=Robot(30) # initialiser le robot
env=Environnement([1000,500],rob,5) # initialiser l'environment
simulation = Simulation(env,100)
simulation.addSimulation(5) #ajouter des obstcales a l'environnement
  
root = Tk() # initialiser la fenetre tkinter
view=View(root, simulation)
view.start_sim()
root.mainloop()
<<<<<<< HEAD

view.stop_sim()

=======
view.stop_sim()
>>>>>>> 26dbab3380f65ceaffe6b6b62f649f5db799b8d0
