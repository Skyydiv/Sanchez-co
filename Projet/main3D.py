from robot.simu import create_simu
from robot.IA import ControleurRobotVirtuel,get_Tracerarre, get_AvancerToutDroit, get_TournerAngle,get_IABoucle,get_Seq_IA,get_Seq_list
from robot.affichage import create_aff3D

#le client fait son choix avec le nombre d'obstacle
simulation=create_simu(4)
# simulation.environnement.addObstacle(600,0,0,0,30)
# simulation.environnement.addObstacle(0,simulation.SIMU_HEIGHT,0,0,30)
# simulation.environnement.addObstacle(simulation.SIMU_WIDTH,0,0,0,30)
# simulation.environnement.addObstacle(simulation.SIMU_WIDTH,simulation.SIMU_HEIGHT,0,0,30)
affichage=create_aff3D(simulation)
cr=ControleurRobotVirtuel(simulation.robot)  #initialiser le controleur  virtuel

#le client fait son choix de la strategie qui souhaite executé
strategie=get_Tracerarre(cr,500,300)
#De plus, le client decide s'il veut repeter cette startegie plusieurs fois,avec le nombre de repetition
iaseq=get_Seq_IA(cr,10,strategie)
#Le client decide quelle stratgie lancer
iaboucle=get_IABoucle(cr,iaseq)

iaboucle.start()
simulation.run_simu()
affichage.run()


