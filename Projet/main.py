from tkinter import *
from robot.affichage import View
from robot.simu.simulation import Simulation
from robot.IA import Ia_Avancer_tout_droit, IATournerAngle, BoucleIA, IAseq, TracerCarre,Hexagone,dessineRectangle,dessineDroite,dessineRectangleDroite
from robot.IA.controleur import ControleurRobotVirtuel, ControleurRobotVraieVie
from time import sleep


delta_simu=60000#taux rafraichissement des données de la simu
delta_affich=1 #taux de rafraichissement de l'affichage
delta_ia=0.000000000001

simulation=Simulation(delta_simu)
simulation.addObstacle4coins(30) #ajouter des obstcales a l'environnement

#ajout du controleur
cr=ControleurRobotVirtuel(simulation.robot)


#ia pour avancer tout droit 
ia1=Ia_Avancer_tout_droit(300,200,cr)

#ia pour tourner 
iaa=IATournerAngle(cr,90,200)

#ia seq 
Carre=TracerCarre(cr,300,200)
Hexa=Hexagone(cr,200,200)
Rec=dessineRectangle(cr,200,200)
droite=dessineDroite(cr,300,200)
Recdroite=dessineRectangleDroite(cr,200,200)

iaseq=IAseq(cr,[Hexa,Hexa,Hexa,Hexa,Hexa,Hexa])


iaboucle=BoucleIA(cr,Recdroite,delta_ia)
iaboucle.start()

root = Tk() # initialiser la fenetre tkinter
view=View(root, simulation,delta_affich)
simulation.run_simu()
root.mainloop()
simulation.stop_simu()
