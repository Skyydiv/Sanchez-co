from .virtuel import Robot, Obstacle, Environnement
from .simulation import Simulation

def create_simu(nb_obs):
    '''       
    Creer un une simulation avec le nombre d'obstacle souhaité
    :param nb_obs : nombre d'obstacle souhaité
    :return : la simulation crée
    '''
    delta_simu=60000 #taux rafraichissement des données de la simu
    simulation=Simulation(delta_simu) #initialisation de la simu
    simulation.addSimulation(nb_obs) #ajouter des obstcales a l'environnement
    return simulation

