from Environnement import Environnement
from Objet import Robot
from Objet import Obstacle
from Simulation import Simulation

env=Environnement(10,10,1)
robot=Robot([1,1])

sim=Simulation(3,1,robot,env)
sim.addSimulation(4)
sim.simu()