from .virtuel import Robot, Obstacle, Environnement
from .simulation import Simulation
from .capteur import Capteur, dist, equationDroitePolaire, intersectionDroiteCercle, plusProche

delta_simu=60000 #taux rafraichissement des données de la simu
simulation=Simulation(delta_simu) #initialisation de la simu
simulation.addSimulation(0) #ajouter des obstcales a l'environnement

