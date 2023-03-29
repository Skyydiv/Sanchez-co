from tkinter import *
from robot.affichage import View
from robot.simu.simulation import Simulation
from robot.IA import Ia_Avancer_tout_droit, IATournerAngle, BoucleIA, IAseq, IAcarre
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
iaa=IATournerAngle(cr,90,200)
iaaa=IATournerAngle(cr,120,200)
iae=IATournerAngle(cr,144,200)

#ia seq 
iaseq=IAseq(cr,[ia1,iaa,ia1,iaa,ia1,iaa,ia1,iaa])
iaseq2=IAseq(cr,[ia1,iaa,ia1,iaa,ia1,iaa,ia1])
iaseq3=IAseq(cr,[iaseq,iaseq2])
iaseq4=IAseq(cr,[ia1,iaaa,ia1,iaaa,ia1,iaaa]) #Tracer un triangle équilateral
iaseq5=IAseq(cr,[ia1,iae,ia1,iae,ia1,iae,ia1,iae,ia1,iae]) #Tracer une étoile


iaboucle=BoucleIA(cr,iaseq5,delta_ia)
iaboucle.start()

#iacarre=IAcarre(cr,100,100,200,delta_ia)
#iacarre.start()

root = Tk() # initialiser la fenetre tkinter
view=View(root, simulation,delta_affich)
simulation.run_simu()
root.mainloop()
simulation.stop_simu()
