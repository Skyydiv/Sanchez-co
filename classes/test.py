from Environnement import Environnement
from Objet import Robot
from Objet import Obstacle
from Simulation import Simulation


robot=Robot([1,1], 4)

env = Environnement([100,120], robot, 1)
assert( (env.coordsmax[0] == 100) and (env.coordsmax[1] == 120) and (env.robot == robot) and (env.precision == 1) and (env.ensemble_obstacles==set()) )
assert( (not(env.estMur(3,30))) and (env.estMur(53, -10)) and (env.estMur(-13,95)) and (env.estMur(0,1)) and (env.estMur(3,0)) and (env.estMur(5,120)) and (env.estMur(100,50)))

#sim=Simulation(3,1,robot,env)
#sim.addSimulation(4)
#sim.simu()