from tkinter import *
from robot.affichage import View
from robot.simu.simulation import Simulation
from robot.IA import Ia_Avancer_tout_droit, IATournerAngle, BoucleIA, IAseq, TracerCarre,TracerUn
from robot.IA.controleur import ControleurRobotVirtuel, ControleurRobotVraieVie
from time import sleep
import tmesolo


# delta_simu=600#taux rafraichissement des données de la simu
# delta_affich=60 #taux de rafraichissement de l'affichage
# delta_ia=0.001

# simulation=Simulation(delta_simu)
# simulation.addSimulation(0) #ajouter des obstcales a l'environnement

# #ajout du controleur
# cr=ControleurRobotVirtuel(simulation.robot)


# #ia pour avancer tout droit 
# ia1=Ia_Avancer_tout_droit(300,200,cr)

# #ia pour tourner 
# iaa=IATournerAngle(cr,90,200)

# #ia seq 
# Carre=TracerCarre(cr,300,200)
# iaseq=IAseq(cr,[Carre,Carre])


# iaboucle=BoucleIA(cr,iaseq,delta_ia)
# iaboucle.start()


# root = Tk() # initialiser la fenetre tkinter
# view=View(root, simulation,delta_affich)
# simulation.run_simu()
# root.mainloop()
# simulation.stop_simu()

# tmesolo.qt1_3()
# tmesolo.qt1_3()

tmesolo.qt2_1()
