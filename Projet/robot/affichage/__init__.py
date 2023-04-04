from .view import View
from tkinter import *
from robot.simu import simulation

delta_affich=1 #taux de rafraichissement de l'affichage

root = Tk() # initialiser la fenetre tkinter
View(root, simulation,delta_affich)