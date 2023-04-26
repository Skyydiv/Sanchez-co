from math import pi, sin, cos, degrees


from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from time import sleep

from direct.stdpy import threading2



class View3D(ShowBase):

    def __init__(self,simulation,delta_affichage):

        ShowBase.__init__(self)
        

        self.simu=simulation
        self.robot=simulation.robot
        self.delta_affichage=delta_affichage/100000
        
        #GRAPHICS

            #SCENE
        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)


        # Apply scale and position transforms on the model.
        # self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setScale(10, 10, 10)
        self.scene.setPos(200, 2000, 0)
        


            #MODELS

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.2, 0.2, 0.2)
        self.pandaActor.reparentTo(self.render)
        # self.pandaActor.setPos(12, 13, 0)

                #ANNIMATION
        # Loop its animation.
        self.pandaActor.loop("walk")


        #CAMERA-------------------------------------------------------------------------------------------------------------------------------------------------------
        
        #ajout d'une tache camera pour avoir une vue FPS---------------------------------------------------------------------------------------------------------------
        # self.taskMgr.add(self.spinCameraTaskFPS, "SpinCameraTaskFPS")
        
        #ajout d'une tache camera pour avoir une vue TPS---------------------------------------------------------------------------------------------------------------
        self.taskMgr.add(self.spinCameraTaskTPS, "SpinCameraTaskTPS")


        #crée un thread pour lancer la fonction updatePos: changer la position du robot
        self.updatePosTH=threading2.Thread(name="updatePosRob",target=self.updatePosRob,args=[],daemon=True)
        print("POSTH",self.updatePosTH.name)
        self.updatePosTH.start()
        
      
    #fonction pour déplacement
    def updatePosRob(self):
        
        while True:
            self.pandaActor.setPos(self.robot.x,self.robot.y,0)
            self.pandaActor.setHpr(degrees(self.robot.orientation)+90,0,0)
            sleep(self.delta_affichage)




    #fonction pour caméra
    # Define a procedure to move the camera.
    #set les valeurs de la caméra (position et orientation)
    def spinCameraTaskFPS(self, task):
    
        # Définir la position de la caméra directement derrière le panda
        camX = self.robot.x + (65*cos(self.robot.orientation))
        camY = self.robot.y + (65*sin(self.robot.orientation))
        camZ = 90
        self.camera.setPos(camX, camY, camZ)
        
        # Orienter la caméra vers l'avant en utilisant l'orientation actuelle du panda
        lookAtX = self.robot.x + (600* cos(self.robot.orientation))
        lookAtY = self.robot.y + (600*sin(self.robot.orientation))
        lookAtZ = 80
        self.camera.lookAt(lookAtX, lookAtY, lookAtZ)
        
        
        return Task.cont

    
    
    #fonction pour caméra
    # Define a procedure to move the camera.
    #set les valeurs de la caméra (position et orientation)
    def spinCameraTaskTPS(self, task):
       self.camera.setPos(352, -1376.4, 1855)
       self.camera.setHpr(-2.5, -46.2, 0.5)
       return Task.cont
    



