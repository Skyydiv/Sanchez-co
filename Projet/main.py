from tkinter import *
from robot.affichage import View
from robot.simu.simulation import Simulation
from robot.IA import Ia_Avancer_tout_droit, IATournerAngle, BoucleIA, IAseq, TracerCarre,launchChangeCondition,Hexagon,lunchDessinHex,strat_un
from robot.IA.controleur import ControleurRobotVirtuel, ControleurRobotVraieVie
from time import sleep


delta_simu=6000000#taux rafraichissement des données de la simu
delta_affich=6 #taux de rafraichissement de l'affichage
delta_ia=0.000000000000001

simulation=Simulation(delta_simu)
simulation.addSimulation(0) #ajouter des obstcales a l'environnement


simulation.environnement.addObstacle(100,100,0,0,50)  #,x,y,h,d,rayon
simulation.environnement.addObstacle(100,Simulation.SIMU_HEIGHT-100,0,0,50)
simulation.environnement.addObstacle(simulation.SIMU_WIDTH-100,100,0,0,50)
simulation.environnement.addObstacle(Simulation.SIMU_WIDTH-100,Simulation.SIMU_HEIGHT-100,0,0,50)

simulation.robot.deposer(Simulation.SIMU_WIDTH/2,Simulation.SIMU_HEIGHT/2)
simulation.robot.dessine(True)


#ajout du controleur
cr=ControleurRobotVirtuel(simulation.robot)


#ia pour avancer tout droit 
ia1=Ia_Avancer_tout_droit(300,200,cr)

#ia pour tourner 
iaa=IATournerAngle(cr,90,200)

#ia seq 
Carre=TracerCarre(cr,300,200)
iaseq=IAseq(cr,[Carre,Carre])

# simulation.robot.dessine(False)




#ia hexa
hex=Hexagon(cr,150,500)
lunchDessinHex(simulation.robot,2)




#ia un
un=strat_un(cr,200, 400)

iaboucle=BoucleIA(cr,un,delta_ia)
iaboucle.start()


root = Tk() # initialiser la fenetre tkinter
view=View(root, simulation,delta_affich)
simulation.run_simu()
root.mainloop()
simulation.stop_simu()
