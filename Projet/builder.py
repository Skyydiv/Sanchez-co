from robot.simu.simulation import Simulation
from robot.IA import Ia_Avancer_tout_droit, IATournerAngle, BoucleIA, IAseq, TracerCarre
from robot.affichage import View
from robot.IA.controleur import ControleurRobotVirtuel, ControleurRobotVraieVie
from tkinter import *

def creation_application(strategie,nb_obstacle,context,delta_simu,delta_affichage,delta_ia,monde):
    simulation=creation_Simu(delta_simu,nb_obstacle)
    controlleur=creation_controleur(simulation,context)
    ia_boucle=creation_strategie(strategie,controlleur,delta_ia)
    affichage=creation_affichage(simulation,delta_affichage,monde) #en 2D couple (view,root) 
    start_simu(ia_boucle,simulation,affichage,monde)


def start_simu(ia_boucle,simulation,affichage,monde):
    ia_boucle.start()
    simulation.run_simu()
    if (monde=="2D"):
        view,root=affichage
        root.mainloop()

def creation_Simu(delta_simu, nb_obstacle):
    simulation=Simulation(delta_simu)
    simulation.addSimulation(nb_obstacle) #ajouter des obstcales a l'environnement
    return simulation

def creation_affichage(simulation,delta_affichage,monde):
    if (monde=="2D"):
        affichage=creation_affichage2D(simulation,delta_affichage)
    # elif (monde=="3D"):
    #     affichage=create_affichage3D(simulation,delta_affichage)
    return affichage

def creation_affichage2D(simulation,delta_affichage):
    root = Tk()
    view=View(root,simulation,delta_affichage)
    affichage=(view,root)
    return affichage

# def creation_affichage3D(simulation,delta_affichage):
#     affichage=View3D(simulation,delta_affichage)
#     return affichage

def creation_controleur(simulation,context):
    if (context=="virtuel"):
        controlleur=ControleurRobotVirtuel(simulation.robot)
    elif (context=="reel"):
        controlleur=ControleurRobotVraieVie(simulation.robot)
    return controlleur

def creation_strategie(strategie,controlleur,delta_ia):
    
    if (strategie=="tourner"):
        ia=IATournerAngle(controlleur,90,200)
    elif (strategie=="carre"):
        ia=TracerCarre(controlleur,300,200)
    elif (strategie=="avancer"):
        ia=Ia_Avancer_tout_droit(300,200,controlleur)
    return BoucleIA(controlleur,ia,delta_ia)