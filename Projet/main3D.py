from robot.simu import create_simu
from robot.IA import ControleurRobotVirtuel,get_Tracerarre, get_AvancerToutDroit, get_TournerAngle,get_IABoucle,get_Seq_IA,get_Seq_list
from robot.affichage import create_aff3D

#le client fait son choix avec le nombre d'obstacle
simulation=create_simu(0)
affichage=create_aff3D(simulation)
cr=ControleurRobotVirtuel(simulation.robot)  #initialiser le controleur  virtuel

#le client fait son choix de la strategie qui souhaite executé
strategie=get_Tracerarre(cr,20,50)
#De plus, le client decide s'il veut repeter cette startegie plusieurs fois,avec le nombre de repetition
iaseq=get_Seq_IA(cr,2,strategie)
#Le client decide quelle stratgie lancer
iaboucle=get_IABoucle(cr,iaseq)

# #TESTER POUR VOIR COMMENT LANCER UNE IASEQ D'UNE LISTE D'IAx²
# strategie1=get_AvancerToutDroit(cr,300,200)
# strategie2=get_TournerAngle(cr,90,200)
# iaseq=get_Seq_list(cr,3,[strategie1,strategie2])
# iaboucle=get_IABoucle(cr,iaseq)


iaboucle.start()
simulation.run_simu()
affichage.run()


