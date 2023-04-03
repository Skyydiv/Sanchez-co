from tkinter import *
from robot.affichage import View
from robot.simu.simulation import Simulation
from robot.IA import Ia_Avancer_tout_droit, IATournerAngle, BoucleIA, IAseq, TracerCarre
from robot.IA.controleur import ControleurRobotVirtuel

def q1_1():
    delta_simu=600
    delta_affich=60 

    simulation=Simulation(delta_simu,750,400)
    simulation.addSimulation() 

    root = Tk() # initialiser la fenetre tkinter
    view=View(root, simulation,delta_affich)
    simulation.run_simu()
    root.mainloop()
    simulation.stop_simu()

#qt1_2 : même que qt1_1


