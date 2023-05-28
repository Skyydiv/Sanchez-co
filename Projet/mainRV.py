from robot.IA import *
from robot2IN013 import Robot2IN013

robot=Robot2IN013()


cr=ControleurRobotVraieVie(robot)  

ia=Ia_Avancer_tout_droit(500,100,cr)
ia2=IATournerAngle(cr,90,100)
iaseq=IAseq(cr,[ia,ia2,ia,ia2,ia,ia2,ia,ia2])
iaboucle=BoucleIA(cr,iaseq,0.4)

iaboucle.start()
