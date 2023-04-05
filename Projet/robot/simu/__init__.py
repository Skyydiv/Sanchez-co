from .virtuel import Robot, Obstacle, Environnement
from .simulation import Simulation

delta_simu=60000 #taux rafraichissement des données de la simu
simulation=Simulation(delta_simu) #initialisation de la simu
simulation.addSimulation(5) #ajouter des obstcales a l'environnement

