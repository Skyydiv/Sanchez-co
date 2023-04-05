from math import pi, sin, cos


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
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        


            #MODELS

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        # self.pandaActor.setPos(12, 13, 0)

                #ANNIMATION
        # Loop its animation.
        self.pandaActor.loop("walk")


        #CAMERA

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        


        #crée un thread pour lancer la fonction updatePos: changer la position du robot
        self.updatePosTH=threading2.Thread(name="updatePosRob",target=self.updatePosRob,args=[],daemon=True)
        print("POSTH",self.updatePosTH.name)
        self.updatePosTH.start()

        

    #fonction pour déplacement
    def updatePosRob(self):
        while True:
            self.pandaActor.setPos(self.robot.x,self.robot.y,0)
            sleep(self.delta_affichage)





    #fonction pour caméra
    # Define a procedure to move the camera.
    #set les valeurs de la caméra (position et orientation)
    def spinCameraTask(self, task):
        # pos=self.camera.getPos()
        # print(pos)

        # hpr=self.camera.getHpr()
        # print(hpr)

        # self.camera.setPos(4.54429, 45.0254, 31.4798)
        # self.camera.setHpr(176.418, -31.9264, -2.79153)

        self.camera.setPos(0, -35, 30)
        self.camera.setHpr(0, -40, 0)


        return Task.cont




