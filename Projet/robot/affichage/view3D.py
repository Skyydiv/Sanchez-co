from math import pi, sin, cos, degrees, sqrt


from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from time import sleep

from direct.stdpy import threading2



class View3D(ShowBase):

    def __init__(self,simulation,delta_affichage,vue):
        """
        Constructeur de la classe View3D
        :param simulation: la simulation
        :param delta_affichage: le temps entre chaque mise à jour de l'affichage
        :param vue: la vue choisie (fps ou haut)
        """

        ShowBase.__init__(self)
        

        self.simu=simulation
        self.env=simulation.environnement
        self.robot=simulation.robot
        self.delta_affichage=delta_affichage/100000
        
        #GRAPHIQUES 

            #SCENE
        #charger le modèle de l'environnement
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        #lie la scene au rendu
        self.scene.reparentTo(self.render)


        
        #applique une transformation de position et de taille(mise à echelle)
        self.scene.setScale(11, 11, 11)
        self.scene.setPos(440, 2000, 0)
        

            #Obstacles
        obs=[]
        i=0
        for ob in self.env.ensemble_obstacles:
            obs.append(self.loader.loadModel("3Dmodels/rock/scene.gltf"))
            # lie l'obstacle au rendu, place à la bonne position et redimensionne
            obs[i].reparentTo(self.render)
            obs[i].setPos(ob.x, ob.y, 0)
            nb=int(sqrt(ob.rayon)*3)
            obs[i].setScale(nb, nb, nb)
            obs[i].setHpr(0, 90, 0)
            i += 1

      
            #MODELS

        # PANDA
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.15, 0.15, 0.15)
        self.pandaActor.reparentTo(self.render)

                #ANNIMATION
        # annimation de marche du panda
        self.pandaActor.loop("walk")


                #CAMERA

        #choix entre vue FPS ou TPS(du dessus)
        
        if (vue=="fps"):
            #ajout d'une tache camera pour avoir une vue FPS---------------------------------------------------------------------------------------------------------------
            self.taskMgr.add(self.CameraTaskFPS, "CameraTaskFPS")
        
        if (vue=="haut"):
            #ajout d'une tache camera pour avoir une vue TPS---------------------------------------------------------------------------------------------------------------
            self.taskMgr.add(self.CameraTaskHaut, "CameraTaskHaut")

  
        #crée un thread pour lancer la fonction updatePos: changer la position du robot
        self.updatePosTH=threading2.Thread(name="updatePosRob",target=self.updatePosRob,args=[],daemon=True)
        print("POSTH",self.updatePosTH.name)
        self.updatePosTH.start()
        
      
    #fonction pour déplacement
    def updatePosRob(self):
        """
        Met à jour la position du robot
        """
        
        while True:
            self.pandaActor.setPos(self.robot.x,self.robot.y,0)
            self.pandaActor.setHpr(degrees(self.robot.orientation)+90,0,0)
            sleep(self.delta_affichage)




    #fonctions pour caméra

    def CameraTaskFPS(self, task):
        """
        Possitionne la caméra au niveau des yeux du panda
        """

        # Définir la position de la caméra directement derrière le panda
        camX = self.robot.x + (65*cos(self.robot.orientation))
        camY = self.robot.y + (65*sin(self.robot.orientation))
        camZ = 90
        self.camera.setPos(camX, camY, camZ)
        
        # Orienter la caméra vers l'avant en utilisant l'orientation actuelle du panda
        lookAtX = self.robot.x + (600* cos(self.robot.orientation))
        lookAtY = self.robot.y + (600*sin(self.robot.orientation))
        lookAtZ = 70
        self.camera.lookAt(lookAtX, lookAtY, lookAtZ)
        
        
        return Task.cont

    
    
    def CameraTaskHaut(self, task):
       """
       Possitionne la caméra au dessus de la scène
       """
       self.camera.setPos(700, -1376.4, 1855)
       self.camera.setHpr(-2.5, -46.2, 0.5)
       return Task.cont
    
