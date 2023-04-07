from .view import View
# from .view3D import View3D
from tkinter import *

delta_affich=10 #taux de rafraichissement de l'affichage

def create_aff2D(simulation):
    """Creer l'affichage 2D de la simulation souhaitée
    :param simulation: simulation souhaitée
    :return : l'affichage 2D crée"""
    root = Tk() # initialiser la fenetre tkinter
    View(root, simulation,delta_affich)
    return root