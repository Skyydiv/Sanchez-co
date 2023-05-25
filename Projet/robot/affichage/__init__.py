from .view import View
from .view3D import View3D
from tkinter import *

delta_affich=10 #taux de rafraichissement de l'affichage

def create_aff2D(simulation):
    """Creer l'affichage 2D de la simulation souhaitée
    :param simulation: simulation souhaitée
    :return : l'affichage 2D crée"""
    root = Tk() # initialiser la fenetre tkinter
    View(root, simulation,delta_affich)
    return root

def create_aff3D(simulation,vue="haut"):
    '''
    créer l'affichage 3D
    :param simulation: simulation souhaitée
    :param vue: vue souhaitée (haut ou fps)
    '''
    simulation.robot._x=-10 #sera supprimer par la suite
    simulation.robot._y=-7  

    affichage=View3D(simulation,delta_affich,vue)
    return affichage
