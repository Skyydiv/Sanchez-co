from robot.simu import create_simu
from robot.IA import ControleurRobotVirtuel,get_Tracerarre, get_AvancerToutDroit, get_TournerAngle,get_IABoucle,get_Seq_IA,get_Seq_list
from robot.affichage import create_aff3D

#le client fait son choix avec le nombre d'obstacle
simulation=create_simu(0)
simulation.environnement.addObstacle(570,570,1,1,30)

affichage=create_aff3D(simulation,"fps")  #initialiser l'affichage visualisation du fps
#affichage=create_aff3D(simulation,"haut")  #initialiser l'affichage visualisation du dessus

cr=ControleurRobotVirtuel(simulation.robot)  #initialiser le controleur  virtuel

#le client fait son choix de la strategie qui souhaite executé
strategie=get_Tracerarre(cr,500,300)
# strategie=get_AvancerToutDroit(cr,200,300)
# strategie=get_TournerAngle(cr,90,100)

#De plus, le client decide s'il veut repeter cette startegie plusieurs fois,avec le nombre de repetition
iaseq=get_Seq_IA(cr,2,strategie)
#Le client decide quelle stratgie lancer
iaboucle=get_IABoucle(cr,iaseq)

iaboucle.start() #lancer la strategie
simulation.run_simu() #lancer la simulation
affichage.run() #lancer l'affichage


