from tkinter import *
from robot.affichage import View
from robot.simu.simulation import Simulation
from robot.IA import Ia_Avancer_tout_droit, IATournerAngleDroite,IATournerAngleGauche, BoucleIA, IAseq, Ia_Cercle, TracerCarre, IA_led,Strategiemotif1
from robot.IA.controleur import ControleurRobotVirtuel, ControleurRobotVraieVie
from time import sleep


delta_simu=600#taux rafraichissement des données de la simu
delta_affich=60 #taux de rafraichissement de l'affichage
delta_ia=0.001

simulation=Simulation(delta_simu)
simulation.addSimulation(0) #ajouter des obstcales a l'environnement

#ajout du controleur
cr=ControleurRobotVirtuel(simulation.robot)


#ia pour avancer tout droit 
ia1=Ia_Avancer_tout_droit(300,200,cr)

#ia pour tourner 
iaa=IATournerAngleDroite(cr,90,200)

#ia led
ialed=IA_led(300,200,cr)

#ia vitessesdiff

ia2=Ia_Cercle(50,200,cr,)
#ia seq 
Carre=TracerCarre(cr,300,200)
iaseq=IAseq(cr,[Carre,Carre])

motif1=Strategiemotif1(cr,300,200)


iaboucle=BoucleIA(cr, motif1,delta_ia)
iaboucle.start()


root = Tk() # initialiser la fenetre tkinter
view=View(root, simulation,delta_affich)
simulation.run_simu()
root.mainloop()
simulation.stop_simu()
