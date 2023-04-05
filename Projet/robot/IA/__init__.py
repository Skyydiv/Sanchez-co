from .IA import Ia_Avancer_tout_droit, IAseq, IATournerAngle,BoucleIA,TracerCarre,IAEviteCrash,IAIfThenElse
from robot.IA.controleur import ControleurRobotVirtuel, ControleurRobotVraieVie
from robot.simu import simulation

delta_ia=0.000000000001

#initialiser le controleur  virtuel
cr=ControleurRobotVirtuel(simulation.robot)

#ia pour avancer tout droit 
ia10=Ia_Avancer_tout_droit(300,200,cr)
#ia pour tourner 
iaa=IATournerAngle(cr,90,200)
#ia seq 
Carre=TracerCarre(cr,300,200)
iaseq=IAseq(cr,[Carre,Carre])
 #ia boucle
iaboucle=BoucleIA(cr,iaseq,delta_ia)