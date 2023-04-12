from .virtuel import Robot, Obstacle, Environnement
from .simulation import Simulation

delta_simu=0.001 #taux rafraichissement des données de la simu

def create_simu(nb_obs):
    '''       
    Creer un une simulation avec le nombre d'obstacle souhaité
    :param nb_obs : nombre d'obstacle souhaité
    :return : la simulation crée
    '''
    simulation=Simulation(delta_simu) #initialisation de la simu
    simulation.addSimulation(nb_obs) #ajouter des obstcales a l'environnement
    return simulation

