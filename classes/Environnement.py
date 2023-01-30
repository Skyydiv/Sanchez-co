import numpy
from Robot import Robot
from Obstacle import Obstacle

class Environnement() :
    ''' L'environnement dans lequel se trouve le Robot'''

    def __init__(self,x,y,echelle):
        '''Constructeur de la classe Environnement, creer un tableau d'ensemble vide de x lignes et y colonnes
        
        :param x: nombre de lignes
        :param y: nombre de colonnes
        :param echelle: échelle 
        '''
        
        self.tab=numpy.empty([int(x),int(y)],dtype=set)  
        for i in range(int(x)):
            for j in range(int(y)):
                self.tab[i][j]=set()
        self.nblignes=int(x)
        self.nbcolonnes=int(y)
        self.echelle=echelle


    def verifieMur(self,x,y):
        '''
        Vérifie si les coordonée x et y sont dans l'enceinte de l'environnement. 
        :param x: coordonné réelle
        :param y: coordonné réelle
        :return False si on est dans l’environnement 
        :return True si on se prend un mur
        '''
        if ((x>=self.nblignes) or (y>=self.nbcolonnes) or (x<=0) or (y<=0)):
            return True
        return False

    def verifieObstacle(self, x, y):
        '''Verfie s'il y a un obstacle dans la case avec les mêmes coordonnées
        :param x: indice de la ligne
        :param y: indice de la colonne
        :returns: True s'il existe déjà un obstacle avec les mêmes coordonnées, False sinon
        '''
        if (self.tab[int(x)][int(y)]==set()):
            return False
        elif self.tab[int(x)][int(y)]!=set(): 
            for i in self.tab[int(x)][int(y)]:
                if i.x==x and i.y==y:
                    return True
        return False
    
    def deposerRobot(self,robot):
        """ Dépose le robot en paramètre s'il y a aucun obstacle dans la case où on veut le poser.
        :param robot: robot à déposer """
        if self.tab[int(robot.x)][int(robot.y)]==set():
            self.tab[int(robot.x)][int(robot.y)].add(robot)
        elif self.tab[int(robot.x)][int(robot.y)]!=set():
            print("Il y a déjà un objet dans cette case veuillez changer les coordonnées du robot ou enlever les objets présents")

    def deposerObstable(self,x,y,h,d):
        """ Dépose les obstacles s'il n'y a pas déjà un objet dans la case avec les mêmes coordonnées en faisant appel à la fonction verifieObstacle
        :param x: Coordonnées x de l'obstacle qu'on va créer*
        :param y: Coordonnées y de l'obstacle qu'on va créer
        :param h: hauteur de l'obstacle
        :param d: distance du sol de l'obstacle
        """
        
        i=True
        ob=Obstacle(x,y,h,d)
        if self.tab[int(x)][int(y)]==set():
            self.tab[int(x)][int(y)].add(ob)
        elif self.tab[int(x)][int(y)]!=set():
            if self.verifieObstacle(x,y):
                print("Il y a déjà un objet dans cette case veuillez changer les coordonnées dans les paramètres de la fonction")
            else:
                self.tab[int(x)][int(y)].add(ob)
    

    def deplacerRobot(self, robot):
        """
            Vérifie si il y a un obstacle aux coordonnés après le déplacement ou si il y a mur sur la route
                si oui on bouge pas
                sinon change les coordonnées x et y du robot
            :param robot: le robot à déplacer
        """
        new_x = robot.x + robot.vitesse[0]
        new_y = robot.y + robot.vitesse[1]
        if (self.verifieObstacle(new_x,new_y)) or (self.verifieMur(new_x,new_y)):
            return
        robot.x = new_x
        robot.y = new_y






                

#test 
env=Environnement(5,10,5)
rob=Robot([1.2,4])
ob1=Obstacle(1.2,3.4,4,5.6)
env.tab[int(ob1.x)][int(ob1.y)].add(ob1)
print(env.verifieObstacle(1.2,3.4))
env.deposerRobot(rob)
env.deposerObstable(1.2,3.5,4,5)



#test2
#env=Environnement(10,10,1)
#rob=Robot([2,0])
#rob.x=0.1
#rob.y=0.1
#env.deposerRobot(rob)
#print(env.tab[0][0]) #robot bien placé


#test verifieMur
#print("nblignes",env.nblignes)
#print("nbcolonnes",env.nbcolonnes)

#print("(3,3) ", env.VerifieMur(3,3)) #ok
#print("(0,3) ", env.VerifieMur(0,3)) #ok
#print("(0.1,3) ", env.VerifieMur(0.1,3)) #ok

#print("(3,0) ", env.VerifieMur(3,0)) #ok
#print("(3,10) ", env.VerifieMur(3,10)) #ok
#print("(10,3) ", env.VerifieMur(10,3)) #ok

#print("(10,10) ", env.VerifieMur(10,10)) #ok
#print("(11,3) ", env.VerifieMur(11,3)) #ok

#test deplacerRobot 
#print("position: ", rob.x,rob.y, "direction: ",rob.vitesse)
#env.deplacerRobot(rob)
#rob.vitesse=[0,-3.4]
#print("position: ", rob.x,rob.y, "direction: ",rob.vitesse)
#env.deplacerRobot(rob)
#rob.vitesse=[0,-3.4]
#print("position: ", rob.x,rob.y, "direction: ",rob.vitesse)