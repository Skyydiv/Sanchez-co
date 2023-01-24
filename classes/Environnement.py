import numpy
from Objet import Robot


class Environnement() :
    ''' L'environnement dans lequel se trouve le Robot'''

    def __init__(self,x,y):
        '''Constructeur de la classe Environnement, creer un tableau vide de robot de x lignes et y colonnes
        
        :param x: nombre de lignes
        :param y: nombre de colonnes
        '''
        self.tab=numpy.empty((int(x),int(y)),Robot)
        self.nblignes=int(x)
        self.nbcolonnes=int(y)

    def afficheTab(self):
        '''Affiche l'environnement dans la console'''
        for ligne in self.tab:
            for elt in ligne:
                if isinstance(elt,Robot):
                    print("R   ", end=", ")
                else :
                    print(elt, end=", ")
            print()


#tests
env=Environnement(5,5)
robot=Robot("droite")
env.afficheTab()
print()
robot.deposer(env,robot.x,robot.y)
print("Le robot a été déposé dans l'environnement")
env.afficheTab()
print()
robot.getPos()
print("La direction du robot est vers", robot.orientation)
robot.avancer(env,3)
robot.getPos()
env.afficheTab()
robot.tourner("bas")
robot.avancer(env,2)
robot.getPos()
env.afficheTab()
robot.tourner("gauche")
robot.avancer(env,4)
env.afficheTab()
robot.tourner("haut")
robot.avancer(env,1)
env.afficheTab()
robot.avancer(env,2)

robot.tourner("droite")
robot.avancer(env,1)
robot.getPos()
env.afficheTab()
print()

robot.reculer(env,2)
robot.getPos()
env.afficheTab()
print()

robot.tourner("haut")
robot.reculer(env,2)
robot.getPos()
env.afficheTab()
print()


robot.tourner("bas")
robot.reculer(env,2)
robot.getPos()
env.afficheTab()
print()

robot.tourner("gauche")
robot.reculer(env,4)
robot.getPos()
env.afficheTab()
print()

robot.tourner("bas")
robot.reculer(env,1)
robot.getPos()
env.afficheTab()
print()
