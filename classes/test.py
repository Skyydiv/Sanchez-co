from environnement import Environnement
from Objet import Robot
from Objet import Obstacle
from simulation import Simulation

env=Environnement(10,10,1)
robot=Robot([0.5,0.5])

sim=Simulation(10,1,robot,env)
sim.addSimulation(3)
sim.simu()