from tkinter import *
from tkinter import ttk
from robot.simu.virtuel import Robot, Environnement
from robot.affichage import View
from robot.simu.simulation import Simulation
from robot.IA import Ia_Avancer_tout_droit
from robot.IA import BoucleIA
from robot.IA import IAseq
from robot.IA.controleur import ControleurRobotVirtuel
import os
import sys
from time import sleep
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


simulation=Simulation(100)
simulation.addSimulation(5) #ajouter des obstcales a l'environnement

#ajout du controleur

cr=ControleurRobotVirtuel(simulation.robot)

        

ia1=Ia_Avancer_tout_droit(simulation.robot,200,100,cr)
ia2=Ia_Avancer_tout_droit(simulation.robot,500,300,cr)
iaseq=IAseq(cr,[ia1,ia2,ia1])
iaboucle=BoucleIA(cr,iaseq)

iaboucle.start()



# iaboucle.start()

root = Tk() # initialiser la fenetre tkinter
view=View(root, simulation)
simulation.run_simu()
# view.start_sim()
root.mainloop()
simulation.stop_simu()
# view.stop_sim()
