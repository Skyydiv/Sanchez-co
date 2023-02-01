from Environnement import Environnement
from Objet import Robot
from Objet import Obstacle
from Simulation import Simulation

env=Environnement(10,5,1)
robot=Robot([0.5,0.5])

simu=Simulation(10,1,robot,env)
