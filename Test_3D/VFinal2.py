from math import pi, sin, cos


from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3
from time import sleep


class MyApp(ShowBase):

    def __init__(self):

        ShowBase.__init__(self)
        # Disable the camera trackball controls.
        #self.disableMouse()

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")

        # Reparent the model to render.
        self.scene.reparentTo(self.render)

        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        

        # Add the spinCameraTask procedure to the task manager.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        self.pandaActor.reparentTo(self.render)
        self.pandaActor.setPos(-12, 13, 0)

        # Loop its animation.
        self.pandaActor.loop("walk")


        # Create the four lerp intervals needed for the panda to
        # deplacement
        posInterval1 = self.pandaActor.posInterval(3,
                                                   (-12, -4, 0),
                                                   startPos=(-12, 13, 0))

        posInterval2 = self.pandaActor.posInterval(3,
                                                   (5, -4, 0),
                                                   startPos=(-12, -4, 0))
        
        posInterval3 = self.pandaActor.posInterval(3,
                                                   (5, 13, 0),
                                                   startPos=(5, -4, 0))

        posInterval4 = self.pandaActor.posInterval(3,
                                                   (-12, 13, 0),
                                                    startPos=(5, 13, 0))
        

        #orientation
        hprInterval1 = self.pandaActor.hprInterval(1,
                                                   (90, 0, 0),
                                                   startHpr=(0, 0, 0))

        hprInterval2 = self.pandaActor.hprInterval(1,
                                                   (180, 0, 0),
                                                   startHpr=Point3(90, 0, 0))

        hprInterval3 = self.pandaActor.hprInterval(1,
                                                   (270, 0, 0),
                                                   startHpr=Point3(180, 0, 0))
        
        hprInterval4 = self.pandaActor.hprInterval(1,
                                                   (360, 0, 0),
                                                   startHpr=Point3(270, 0, 0))




        # Create and play the sequence that coordinates the intervals.

        # self.pandaPace = Sequence(posInterval1, hprInterval1,
        #                           posInterval2, hprInterval2,
        #                           name="pandaPace")
        self.pandaPace = Sequence(posInterval1,hprInterval1,
                                  posInterval2,hprInterval2,
                                  posInterval3, hprInterval3,
                                  posInterval4,hprInterval4)
        self.pandaPace.loop()


        #positioning camera
       # self.camera.setPos(100, 0, 30)
        #orienté la caméra
        #self.camera.setHpr(0, -90, 0)


    # Define a procedure to move the camera.
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(0, -35, 30)
        self.camera.setHpr(0, -40, 0)

        return Task.cont




app = MyApp()

app.run()