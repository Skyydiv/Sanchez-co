from robot.simu import create_simu
from robot.IA import ControleurRobotVirtuel,get_Tracerarre, get_AvancerToutDroit, get_TournerAngle,get_IABoucle,get_Seq_IA,get_Seq_list
from robot.affichage import create_aff2D

#le client fait son choix avec le nombre d'obstacle
simulation=create_simu(10)
root=create_aff2D(simulation)
cr=ControleurRobotVirtuel(simulation.robot)  #initialiser le controleur  virtuel

#le client fait son choix de la strategie qui souhaite executé
strategie1=get_AvancerToutDroit(cr,10000,200)
strategie=get_Tracerarre(cr,400,400)
#De plus, le client decide s'il veut repeter cette startegie plusieurs fois,avec le nombre de repetition
iaseq=get_Seq_IA(cr,2,strategie)
#Le client decide quelle stratgie lancer
iaboucle=get_IABoucle(cr,strategie1)

# #TESTER POUR VOIR COMMENT LANCER UNE IASEQ D'UNE LISTE D'IA
# strategie1=get_AvancerToutDroit(cr,300,200)
# strategie2=get_TournerAngle(cr,90,200)
# iaseq=get_Seq_list(cr,3,[strategie1,strategie2])
# iaboucle=get_IABoucle(cr,iaseq)

iaboucle.start()
simulation.run_simu()
root.mainloop()
simulation.stop_simu()




