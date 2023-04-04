from robot.simu.simulation import Simulation
from robot.IA import Ia_Avancer_tout_droit, IATournerAngle, BoucleIA, IAseq, TracerCarre
from robot.affichage import View
from robot.IA.controleur import ControleurRobotVirtuel, ControleurRobotVraieVie
from tkinter import *

def creation_application(strategie,nb_obstacle,context,delta_simu,delta_affichage,delta_ia,monde):
    '''
    Lance tout ce qui est nécessaire pour démarer l'applicaiton
    :param strategie: la strategie de l'IA
    :param nb_obstacle: le nombre d'obstacle dans l'environnement
    :param context: le contexte de l'IA (virtuel ou réel)
    :param delta_simu: le taux de rafraichissement de la simulation (ordre de grandeur 10^6)
    :param delta_affichage: le taux de rafraichissement de l'affichage (ordre de grandeur 1)
    :param delta_ia: le taux de rafraichissement de l'IA (ordre de grandeur 10^-7)
    :param monde: le monde dans lequel on se trouve (2D ou 3D)
    '''
    simulation=creation_Simu(delta_simu,nb_obstacle)
    controlleur=creation_controleur(simulation,context)
    ia_boucle=creation_strategie(strategie,controlleur,delta_ia)
    affichage=creation_affichage(simulation,delta_affichage,monde) #en 2D couple (view,root) 
    start_simu(ia_boucle,simulation,affichage,monde)


def start_simu(ia_boucle,simulation,affichage,monde):
    '''
    Lance la simulation, l'affichage et la boucle de l'IA
    '''
    ia_boucle.start()
    simulation.run_simu()
    if (monde=="2D"):
        view,root=affichage
        root.mainloop()

def creation_Simu(delta_simu, nb_obstacle):
    '''
    Creer la simulation
    '''
    simulation=Simulation(delta_simu)
    simulation.addSimulation(nb_obstacle) #ajouter des obstcales a l'environnement
    return simulation

def creation_affichage(simulation,delta_affichage,monde):
    '''
    créer l'affichage
    '''
    if (monde=="2D"):
        affichage=creation_affichage2D(simulation,delta_affichage)
    # elif (monde=="3D"):
    #     affichage=create_affichage3D(simulation,delta_affichage)
    return affichage

def creation_affichage2D(simulation,delta_affichage):
    '''
    créer l'affichage 2D
    '''
    root = Tk()
    view=View(root,simulation,delta_affichage)
    affichage=(view,root)
    return affichage

# def creation_affichage3D(simulation,delta_affichage):
#     '''
#     créer l'affichage 3D
#     '''
#     affichage=View3D(simulation,delta_affichage)
#     return affichage

def creation_controleur(simulation,context):
    '''
    créer le controleur
    '''
    if (context=="virtuel"):
        controlleur=ControleurRobotVirtuel(simulation.robot)
    elif (context=="reel"):
        controlleur=ControleurRobotVraieVie(simulation.robot)
    return controlleur

def creation_strategie(strategie,controlleur,delta_ia):
    '''
    créer la strategie
    '''
    if (strategie=="tourner"):
        ia=IATournerAngle(controlleur,90,200)
    elif (strategie=="carre"):
        ia=TracerCarre(controlleur,300,200)
    elif (strategie=="avancer"):
        ia=Ia_Avancer_tout_droit(300,200,controlleur)
    return BoucleIA(controlleur,ia,delta_ia)