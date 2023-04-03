from tkinter import *
from robot.affichage import View
from robot.simu.simulation import Simulation
from robot.IA import Ia_Avancer_tout_droit, IATournerAngle, BoucleIA, IAseq, TracerCarre
from robot.IA.controleur import ControleurRobotVirtuel, ControleurRobotVraieVie
from time import sleep


delta_simu=600#taux rafraichissement des données de la simu
delta_affich=60 #taux de rafraichissement de l'affichage
delta_ia=0.001

simulation=Simulation(delta_simu)
simulation.addSimulation() #ajouter des obstcales a l'environnement

#ajout du controleur
cr=ControleurRobotVirtuel(simulation.robot)



simulation.robot.dessine(True)#choisir de desactiver ou non le crayon <---------------------------

#ia pour avancer tout droit 
ia=Ia_Avancer_tout_droit(100,200,cr)
ia1=Ia_Avancer_tout_droit(300,200,cr)

#ia pour tourner 
iaa40=IATournerAngle(cr,40,200)
iaa50=IATournerAngle(cr,50,200)
iaa90=IATournerAngle(cr,90,200)
#ia seq 
Carre=TracerCarre(cr,300,200)


iaPour1=IAseq(cr,[iaa90,ia1])#strategie pour dessiner un 1


iaPour0=IAseq(cr,[ia,iaa90,ia1,iaa90,ia,iaa90,ia1])#strategie pour dessiner un 0


iaseq=IAseq(cr,[ia,iaa,ia,ia1,ia,iaa,ia,ia1,ia,iaa,ia,ia1,ia,iaa,ia,iaa,ia])


iaPour0puis1=IAseq(cr,[iaPour0,iaa90,ia1,iaPour1])

iaboucle=BoucleIA(cr,iaPour0puis1,delta_ia)
iaboucle.start()


root = Tk() # initialiser la fenetre tkinter
view=View(root, simulation,delta_affich)
simulation.run_simu()
root.mainloop()
simulation.stop_simu()
