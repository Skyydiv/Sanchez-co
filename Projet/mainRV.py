from robot.IA import ControleurRobotVraieVie,get_Tracerarre, get_AvancerToutDroit, get_TournerAngle,get_IABoucle,get_Seq_IA,get_Seq_list
from robot2IN013 import Robot2IN013 as robot

#le client fait son choix avec le nombre d'obstacle
cr=ControleurRobotVraieVie(robot)  #initialiser le controleur  vrai vie

#le client fait son choix de la strategie qui souhaite executé
strategie=get_Tracerarre(cr,300,200)
#De plus, le client decide s'il veut repeter cette startegie plusieurs fois,avec le nombre de repetition
iaseq=get_Seq_IA(cr,2,strategie)
#Le client decide quelle stratgie lancer
iaboucle=get_IABoucle(cr,iaseq)