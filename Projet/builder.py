from robot.simu.simulation import Simulation
from robot.IA import Ia_Avancer_tout_droit, IATournerAngle, BoucleIA, IAseq, TracerCarre,IAIfThenElse,IAEviteCrash
from robot.affichage import View, View3D
from robot.IA.controleur import ControleurRobotVirtuel, ControleurRobotVraieVie
from tkinter import *

def creation_application(strategie,nb_obstacle,context,delta_simu,delta_affichage,delta_ia,monde):
    """Fontion permettant de créer une application avec les paramètres donnés

    Args:
        strategie : strategie de l'IA
        nb_obstacle : nombre d'obstacle dans l'environnement
        context : contexte de l'application (virtuel ou réel)
        delta_simu : pas de temps de la simulation
        delta_affichage : pas de temps de l'affichage
        delta_ia : pas de temps de l'IA
        monde : monde de l'application (2D ou 3D)
    """
    simulation=creation_Simu(delta_simu,nb_obstacle)
    controlleur=creation_controleur(simulation,context)
    ia_boucle=creation_strategie(strategie,controlleur,delta_ia,monde)
    affichage=creation_affichage(simulation,delta_affichage,monde) #en 2D couple (view,root) 
    start_simu(ia_boucle,simulation,affichage,monde)


def start_simu(ia_boucle,simulation,affichage,monde):
    """Fonction permettant de lancer une application

    Args:
        ia_boucle : boucle de l'IA
        simulation : simulation de l'application
        affichage : affichage de l'application
        monde : monde de l'application (2D ou 3D)
    """
    ia_boucle.start()
    simulation.run_simu()
    if (monde=="2D"):
        view,root=affichage
        root.mainloop()
    if (monde=="3D"):
        affichage.run()

def creation_Simu(delta_simu, nb_obstacle):
    """Fonction permettant de créer une simulation

    Args:
        delta_simu : pas de temps de la simulation
        nb_obstacle : nombre d'obstacle dans l'environnement


    """
    simulation=Simulation(delta_simu)
    simulation.addSimulation(nb_obstacle) #ajouter des obstcales a l'environnement
    return simulation

def creation_affichage(simulation,delta_affichage,monde):
    """Fonction permettant de créer un affichage
    
    Args:
        simulation : simulation de l'application
        delta_affichage : pas de temps de l'affichage
        monde : monde de l'application (2D ou 3D)
        
        
    """
    if (monde=="2D"):
        affichage=creation_affichage2D(simulation,delta_affichage)
    elif (monde=="3D"):
        affichage=creation_affichage3D(simulation,delta_affichage)
    return affichage

def creation_affichage2D(simulation,delta_affichage):
    """Fonction permettant de créer un affichage 2D

    Args:
        simulation : simulation de l'application
        delta_affichage : pas de temps de l'affichage

    
    """
    root = Tk()
    view=View(root,simulation,delta_affichage)
    affichage=(view,root)
    return affichage

def creation_affichage3D(simulation,delta_affichage):
    '''
    créer l'affichage 3D
    '''
    simulation.robot._x=-10 #sera supprimer par la suite
    simulation.robot._y=-7  

    affichage=View3D(simulation,delta_affichage)
    return affichage

def creation_controleur(simulation,context):
    """Fonction permettant de créer un controleur

    Args:
        simulation : simulation de l'application
        context : contexte de l'application (virtuel ou réel)

    
    """
    if (context=="virtuel"):
        controlleur=ControleurRobotVirtuel(simulation.robot)
    elif (context=="reel"):
        controlleur=ControleurRobotVraieVie(simulation.robot)
    return controlleur

def creation_strategie(strategie,controlleur,delta_ia,monde):
    """Fonction permettant de créer une strategie

    Args:
        strategie : strategie de l'IA
        controlleur : controleur de l'application
        delta_ia : pas de temps de l'IA

    
    """
    
    vitesse= 200
    distance=300
    if (monde=="3D"): #sera supprimer par la suite, monde aussi
        vitesse/=15
        distance/=15
        
    if (strategie=="tourner"):
        ia=IATournerAngle(controlleur,90,vitesse)
    elif (strategie=="carre"):
        ia=TracerCarre(controlleur,distance,vitesse)
    elif (strategie=="avancer"):
        ia=Ia_Avancer_tout_droit(distance,vitesse,controlleur)
    return BoucleIA(controlleur,ia,delta_ia)