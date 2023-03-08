import math

class Robot:

  WHEEL_BASE_WIDTH=117 # distance (mm) de la roue gauche a la roue droite.
  WHEEL_DIAMETER=66.5 # diametre de la roue (mm)
  WHEEL_BASE_CIRCUMFERENCE =WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
  WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * math.pi # perimetre de la roue (mm)


  def __init__(self,rayon,capteur):
    '''Constructeur de la classe Robot,représentation sous forme de cercle avec des coordonnées par défaut le coin haut gauche (rayon+0.1, rayon+0.1) 
    :param rayon: rayon de l'objet (en mm)
    '''
    self.rayon = rayon

    self.x =0.1+self.rayon #pour être dans l'env
    self.y = 0.1+self.rayon

    
    self.orientation=0 #(radians)
    self.capteur=capteur #Capteur du robot

    # self.MOTOR_LEFT=0 #dps
    # self.MOTOR_RIGHT=0 #dps


    self.MOTOR_LEFT_Offset=0
    self.MOTOR_RIGHT_Offset=0

    self.vitesseRoueDroite=0 #degre par sec
    self.vitesseRoueGauche=0 #degre par sec


  def set_motor_dps(self, port, dps):
    """
    Fixe la vitesse d'un moteur en nombre de degres par seconde
    :port: une constante moteur,  MOTOR_LEFT ou MOTOR_RIGHT (ou les deux MOTOR_LEFT+MOTOR_RIGHT).
    :dps: la vitesse cible en nombre de degres par seconde
    """

    if(port==self.MOTOR_RIGHT):
      self.MOTOR_RIGHT=dps
    if(port==self.MOTOR_LEFT):
      self.MOTOR_LEFT=dps
    if(port==(self.MOTOR_RIGHT,self.MOTOR_LEFT)):
      self.MOTOR_RIGHT=dps
      self.MOTOR_LEFT=dps


  def deplacer(self, intervalle_temps):
        """deplace le robot dans un intervalle de temps
        :param intervalle_temps: intervalle de temps dans lequel le robot avance"""

        #Conversion de la vitesse dps en mm par sec
        vD=self.vitesseRoueDroite/360.0 * math.pi * self.WHEEL_DIAMETER
        vG=self.vitesseRoueGauche/360.0 * math.pi * self.WHEEL_DIAMETER

        distance_parcourue_droite = vD * intervalle_temps
        distance_parcourue_gauche = vG * intervalle_temps

        newOrientation = (distance_parcourue_droite - distance_parcourue_gauche) / self.WHEEL_BASE_WIDTH
        self.orientation += newOrientation

        newV = (distance_parcourue_droite + distance_parcourue_gauche) / 2 #calcul vitesse lineare 
        self.x += newV * math.cos(self.orientation)
        self.y += newV * math.sin(self.orientation)

        # v=(self.vitesseRoueGauche + self.vitesseRoueDroite) / 2 #vitesse lineaire
        # w=(self.vitesseRoueDroite - self.vitesseRoueGauche) / self.WHEEL_BASE_WIDTH #vitesse angulaire


        # distance_parcourue_droite = self.vitesseRoueDroite* intervalle_temps
        # distance_parcourue_gauche = self.vitesseRoueGauche * intervalle_temps

        # newOrientation = (distance_parcourue_droite - distance_parcourue_gauche) / self.WHEEL_BASE_WIDTH
        # self.orientation += newOrientation

        # newV = (distance_parcourue_droite + distance_parcourue_gauche) / 2 #recalcul vitesse lineare parcourue par le robot
        # self.x += newV * math.cos(self.orientation)
        # self.y += newV * math.sin(self.orientation)

  def setVitesse(self,Vr,Vg):
    """set la vitesse des roues
    :param Vr : vitesse de la roue droite
    :param Vg : vitesse de la roue gauche"""
    self.vitesseRoueDroite=Vr
    self.vitesseRoueGauche=Vg


  def get_distance_roue(self,delta_t):
    """
    Lit la distance parcourue par les roues pendant un temps
    :return: couple du distance parcourue par les roues
    """
    rotationrg = (self.vitesseRoueGauche * delta_t)
    distancerg = (math.pi * self.WHEEL_DIAMETER/2 * rotationrg) / 180
    rotationrd = (self.vitesseRoueDroite * delta_t)
    distancerd = (math.pi * self.WHEEL_DIAMETER/2 * rotationrd) / 180
    return (distancerg, distancerd)


class Obstacle :
  '''Obstacle qui peuvent être présent dans l'environnement'''
    
  def __init__(self,x,y,h,d,rayon):
      '''Construteur de l'objet Obstacle, représenter par un cercle , qui initialise les coordonnées, la hauteur, et la distance du sol et le rayon.
      :param x: coordonnée des abscisses (en cm)
      :param y: coordonnée des ordonnées (en cm)
      :param h: hauteur de l'obstacle (en cm)
      :paran d: distance du sol (en cm)
      :param rayon: rayon de l'obstacle
      '''
      self.x=x
      self.y=y
      self.hauteur=h
      self.distSol=d
      self.rayon= rayon

  
class Environnement :
    ''' L'environnement dans lequel se trouve le Robot'''

    def __init__(self,coordsmax,robot,precision):
        '''Constructeur de la classe Environnement : avec des valeurs flottantes pour la taille de l'environnement. 
        L'environnement possede un ensemble d'obstacle qui contient tous les obstacles présents.
        
        :param coordsmax: coordsmax[0] représente la longueur et coordsmax[1] représente la largeur de l'espace (en cm)
        :param robot: le robot unique présent dans l'environnement
        :param precision: le plus petit écart entre 2 points pour les considérer distincts (en cm)
        '''
        self.coordsmax=coordsmax
        self.robot=robot
        self.precision=precision
        self.ensemble_obstacles= set()


    def estMur(self,x,y,rayon):
        '''
        Vérifie si les coordonée x et y sont dans l'enceinte de l'environnement. 
        :param x: coordonné réelle
        :param y: coordonné réelle
        :return False si on est dans l’environnement 
        :return True si on se prend un mur
        '''
        if ((x+rayon>=self.coordsmax[0]) or (y+rayon>=self.coordsmax[1]) or (x-rayon<=0) or (y-rayon<=0)):
            return True
        return False
    
    def estRobot(self,x, y,r):
        """Verifie si les coordonnées passées en parametre se trouve sur la surface du robot
        :param x: coordonnées en x
        :param y: coordonnées en y
        :param r:rayon en mm
        """
        if(self.robot.x+self.robot.rayon>=x-r and self.robot.x-self.robot.rayon<=x+r and self.robot.y+self.robot.rayon>=y-r and self.robot.y-self.robot.rayon<=y+r):
            return True

    def estObstacle(self, x, y,r):
        '''Verfie s'il y a un obstacle dans l'environnement avec les mêmes coordonnées
        :param x: coordonnées en x
        :param y: coordonnées en y
        :param r:rayon en mm
        :returns: True s'il existe déjà un obstacle avec les mêmes coordonnées, False sinon
        '''
        for i in self.ensemble_obstacles:
            if i.x+i.rayon>=x-r and i.x-i.rayon<=x+r and i.y+i.rayon>=y-r and i.y-i.rayon<=y+r:
                return True
        return False

    
    def addObstacle(self,x,y,h,d,rayon):
        """Créer et dépose l'obstacle s'il n'y a pas déjà un objet dans la case avec les mêmes coordonnées en faisant appel à la fonction estObstacle
        :param x: Coordonnées x de l'obstacle qu'on va créer
        :param y: Coordonnées y de l'obstacle qu'on va créer
        :param h: hauteur de l'obstacle
        :param d: distance du sol de l'obstacle
        """
        if not (self.estObstacle(x,y,rayon) and self.estMur(x,y,rayon) and self.estRobot):
            self.ensemble_obstacles.add(Obstacle(x,y,h,d,rayon))
        return

    def calculDistance(self, objet1, objet2):
        '''
        Calcule la distance entre deux objets passer en paramètre, en prenant compte le rayon le rayon des objets. Les objets peuvent être des robots ou des obstacles.
        :param objet1 : robot/obstacle
        :param objet2 : robot/obstacle
        :return : valeur négative ou égale à 0 si les objects sont en collision (ne gère pas la hauteur)
        :return : sinon valeur positive correspondant à la distance en valeur absolue la plus petite entre les 2 rayons (distance générale, ne pdonne pas la direction)
        '''


        return math.sqrt(math.pow(objet1.x-objet2.x,2)+ math.pow(objet1.y-objet2.y,2) - (objet1.rayon + objet2.rayon) )


    
    def detectCollision(self):
        '''
        verifie si les coordonnes du robot sont identiques a un obstacle de l’environnement ou s’il a pris un mur selon une precision
        '''
        return self.estObstacle(self.robot.x,self.robot.y,self.robot.rayon) or self.estMur(self.robot.x,self.robot.y,self.robot.rayon)

