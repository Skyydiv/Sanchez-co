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

ia1=Ia_Avancer_tout_droit(100,100,cr)
iaa=IATournerAngle(cr,90,200)
iaseq=IAseq(cr,[ia1,iaa,ia1,iaa,ia1,iaa,ia1])
iaboucle=BoucleIA(cr,iaseq,delta_ia)
iaboucle.start()

#iacarre=IAcarre(cr,100,100,200,delta_ia)
#iacarre.start()



# iaboucle.start()

root = Tk() # initialiser la fenetre tkinter
view=View(root, simulation,delta_affich)
simulation.run_simu()
root.mainloop()
simulation.stop_simu()
