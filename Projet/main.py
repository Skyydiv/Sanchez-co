from tkinter import *
from robot.affichage import View
from robot.simu.simulation import Simulation
from robot.IA import Ia_Avancer_tout_droit, IATournerAngle, BoucleIA, IAseq
from robot.IA.controleur import ControleurRobotVirtuel, ControleurRobotVraieVie
from time import sleep


delta_simu=600#taux rafraichissement des données de la simu
delta_affich=60 #taux de rafraichissement de l'affichage
delta_ia=0.001

simulation=Simulation(delta_simu)
simulation.addSimulation(0) #ajouter des obstcales a l'environnement

#ajout du controleur

cr=ControleurRobotVirtuel(simulation.robot)

        

ia1=Ia_Avancer_tout_droit(200,100,cr)
ia2=Ia_Avancer_tout_droit(500,300,cr)
iaa=IATournerAngle(cr,90,100)
iaseq=IAseq(cr,[ia1,iaa,ia1,iaa,ia1,iaa,ia1])
iaboucle=BoucleIA(cr,iaseq,delta_ia)
iaboucle.start()



# iaboucle.start()

root = Tk() # initialiser la fenetre tkinter
view=View(root, simulation,delta_affich)
simulation.run_simu()
root.mainloop()
simulation.stop_simu()
