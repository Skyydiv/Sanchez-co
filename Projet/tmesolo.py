from tkinter import *
from robot.affichage import View
from robot.simu.simulation import Simulation
from robot.IA import Ia_Avancer_tout_droit, IATournerAngle, BoucleIA, IAseq, TracerCarre, TracerUn, TracerZero, Tracer01
from robot.IA.controleur import ControleurRobotVirtuel

def qt1_1():
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


def qt1_3():
    delta_simu=600
    delta_affich=60 
    delta_ia=0.001

    simulation=Simulation(delta_simu,500,500)
    simulation.addSimulation()
    simulation.robot.dessine(True)

    #ajout du controleur
    cr=ControleurRobotVirtuel(simulation.robot)

    #ia pour avancer tout droit 
    ia1=Ia_Avancer_tout_droit(300,200,cr)

    iaboucle=BoucleIA(cr,ia1,delta_ia)
    iaboucle.start()

    root = Tk() # initialiser la fenetre tkinter
    view=View(root, simulation,delta_affich)
    simulation.run_simu()
    root.mainloop()
    simulation.stop_simu()

def qt2_1():
    delta_simu=600
    delta_affich=60 
    delta_ia=0.001

    simulation=Simulation(delta_simu,200,200)
    simulation.addSimulation()

    #ajout du controleur
    cr=ControleurRobotVirtuel(simulation.robot)

    UN=TracerUn(cr,200,200,True)

    iaboucle=BoucleIA(cr,UN,delta_ia)
    iaboucle.start()

    root = Tk() # initialiser la fenetre tkinter
    view=View(root, simulation,delta_affich)
    simulation.run_simu()
    root.mainloop()
    simulation.stop_simu()

def qt2_2():
    delta_simu=600
    delta_affich=60 
    delta_ia=0.001

    simulation=Simulation(delta_simu,200,200)
    simulation.addSimulation()

    #ajout du controleur
    cr=ControleurRobotVirtuel(simulation.robot)

    Zero=TracerZero(cr,100,200,200,True)

    iaboucle=BoucleIA(cr,Zero,delta_ia)
    iaboucle.start()

    root = Tk() # initialiser la fenetre tkinter
    view=View(root, simulation,delta_affich)
    simulation.run_simu()
    root.mainloop()
    simulation.stop_simu()


def qt2_4():
    delta_simu=600
    delta_affich=60 
    delta_ia=0.001

    simulation=Simulation(delta_simu,200,200)
    simulation.addSimulation()

    #ajout du controleur
    cr=ControleurRobotVirtuel(simulation.robot)

    zeroUn=Tracer01(cr,100,200,200)

    iaboucle=BoucleIA(cr,zeroUn,delta_ia)
    iaboucle.start()

    root = Tk() # initialiser la fenetre tkinter
    view=View(root, simulation,delta_affich)
    simulation.run_simu()
    root.mainloop()
    simulation.stop_simu()
