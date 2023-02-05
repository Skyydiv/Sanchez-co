from Environnement import Environnement
from Objet import Robot
from Objet import Obstacle
from Simulation import Simulation
from view import View

robot=Robot(2, 3, 4)
obs = Obstacle(10, 0.1, 0, 0, 2)
obs2 = Obstacle(10, 100, 0, 0, 2)
obs3 = Obstacle(10, 0.1, 0, 0, 9)

env = Environnement([100,120], robot, 1)
#test constructeur environnement
assert( (env.coordsmax[0] == 100) and (env.coordsmax[1] == 120) and (env.robot == robot) and (env.precision == 1) and (env.ensemble_obstacles==set()) )

#test méthode estMur de Environnement
assert( (not(env.estMur(3,30))) and (env.estMur(53, -10)) and (env.estMur(-13,95)) and (env.estMur(0,1)) and (env.estMur(3,0)) and (env.estMur(5,120)) and (env.estMur(100,50)))

#test méthode calculDistance de Environnement
assert((env.calculDistance(robot, obs) > 0) and (env.calculDistance(robot, obs3) < 0 )

#sim=Simulation(3,1,robot,env)
#sim.addSimulation(4)
#sim.simu()