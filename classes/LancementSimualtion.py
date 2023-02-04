from tkinter import *
from tkinter import ttk
from Simulation import Simulation
from view import View 

# initialiser le robot
# initialiser l'environment
#ajouter le robot a l'emvironnement
#ajoouer des obstcales a l'environnement

simulation = Simulation(10000,env)
simulation.run() #lancer la simulation
    
root = Tk() # initialiser la fenetre tkinter
Affichage = View(root, simulation)
root.mainloop()
simulation.stop()