import math
from .capteur import Capteur

class Robot:

  WHEEL_BASE_WIDTH=117 # distance (mm) de la roue gauche a la roue droite.
  WHEEL_DIAMETER=66.5 # diametre de la roue (mm)
  WHEEL_BASE_CIRCUMFERENCE =WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
  WHEEL_CIRCUMFERENCE = WHEEL_DIAMETER * math.pi # perimetre de la roue (mm)


  def __init__(self,rayon):
    '''Constructeur de la classe Robot,représentation sous forme de cercle avec des coordonnées par défaut le coin haut gauche (rayon+0.1, rayon+0.1) 
    :param rayon: rayon de l'objet (en mm)
    '''
    self.rayon = rayon

    self._x =100.1+self.rayon #pour être dans l'env
    self._y = 100.1+self.rayon

    
    self._orientation=0 #(radians)
    self.capteur=Capteur(0) #Capteur du robot


    self.MOTOR_LEFT_Offset=0
    self.MOTOR_RIGHT_Offset=0

    self.vitesseRoueDroite=0 #degre par sec
    self.vitesseRoueGauche=0 #degre par sec

    self._distance_parcourue_roue_gauche=0 #en mm
    self._distance_parcourue_roue_droite=0 #en mm

    self._angle_parcouru=0 #(en degre)

  @property
  def x(self):
    """Renvoie coordonnées x du robot"""
    return self._x
  
  @property
  def y(self):
    """Renvoie coordonnées y du robot"""
    return self._y
  
  @property
  def orientation(self):
    """Renvoie coordonnées y du robot"""
    return self._orientation
  
  @property
  def distance_parcourue_roue_gauche(self):
    """Renvoie la distance parcourue par la roue gauche"""
    return self._distance_parcourue_roue_gauche
  
  @property
  def distance_parcourue_roue_droite(self):
    """Renvoie la distance parcourue par la roue droite"""
    return self._distance_parcourue_roue_droite
  
  def set_distance_parcourue_roue_gauche(self,d):
     """fixe la distance_parcourue_roue_gauche a une distance d 
     :param d: distance parcourue"""
     self._distance_parcourue_roue_gauche=d

  def set_distance_parcourue_roue_droite(self,d):
     """fixe la distance_parcourue_roue_droite a une distance d 
     :param d: distance parcourue"""
     self._distance_parcourue_roue_droite=d

  def set_angle_parcouru(self,a ):
     """fixe l'angle_parcouru a un angle a
     :param a: angle parcouru en degre"""
     self._angle_parcouru=a




  def deplacer(self, intervalle_temps):
        """deplace le robot dans un intervalle de temps
        :param intervalle_temps: intervalle de temps dans lequel le robot avance"""

        #Conversion de la vitesse dps en mm par sec
        vD=self.vitesseRoueDroite/360.0 * math.pi * self.WHEEL_DIAMETER
        vG=self.vitesseRoueGauche/360.0 * math.pi * self.WHEEL_DIAMETER

        distance_parcourue_droite = vD * intervalle_temps
        distance_parcourue_gauche = vG * intervalle_temps

        newOrientation = (distance_parcourue_droite - distance_parcourue_gauche) / self.WHEEL_BASE_WIDTH
        self._orientation += newOrientation

        newV = (distance_parcourue_droite + distance_parcourue_gauche) / 2 #calcul vitesse lineare 
        self._x += newV * math.cos(self._orientation)
        self._y += newV * math.sin(self._orientation)

  def setVitesse(self,Vr,Vg):
    """set la vitesse des roues
    :param Vr : vitesse de la roue droite
    :param Vg : vitesse de la roue gauche"""
    self.vitesseRoueDroite=Vr
    self.vitesseRoueGauche=Vg

  def setVitesseRoueDroite(self,v):
    """set la vitesse de la roue droite
    :param v : vitesse de la roue droite
    """
    self.vitesseRoueDroite=v

  def setVitesseRoueGauche(self,v):
    """set la vitesse de la roue gauche
    :param v : vitesse de la roue gauche
    """
    self.vitesseRoueGauche=v

  def stop(self):
    """stop le robot"""
    self.vitesseRoueDroite=0
    self.vitesseRoueGauche=0


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
      self._x=x
      self._y=y
      self._hauteur=h
      self.distSol=d
      self.rayon= rayon
      
  @property
  def x(self):
    """Renvoie coordonnées x de l'obstacle"""
    return self._x
    
  @property
  def y(self):
    """Renvoie coordonnées y de l'obstacle"""
    return self._y
      
class Environnement :
    ''' L'environnement dans lequel se trouve le Robot'''

    def __init__(self,coordsmax,robot : Robot,precision):
        '''Constructeur de la classe Environnement : avec des valeurs flottantes pour la taille de l'environnement. 
        L'environnement possede un ensemble d'obstacle qui contient tous les obstacles présents.
        
        :param coordsmax: coordsmax[0] représente la longueur et coordsmax[1] représente la largeur de l'espace (en cm)
        :param robot: le robot unique présent dans l'environnement
        :param precision: le plus petit écart entre 2 points pour les considérer distincts (en mm)
        '''
        self._coordsmax=coordsmax
        self._robot=robot
        self._precision=precision
        self._ensemble_obstacles= set()

    @property
    def robot(self):
      """Renvoie le robot de l'environnement"""
      return self._robot
      
    @property
    def coordsXmax(self):
      """Renvoie les coordonnées x de l'environnement"""
      return self._coordsmax[0]
    
    @property
    def coordsYmax(self):
      """Renvoie les coordonnées y de l'environnement"""
      return self._coordsmax[1]
    
    @property
    def ensemble_obstacles(self):
       """Renvoie l'ensemble des obstacles de l'environnement"""
       return self._ensemble_obstacles
        
    @property
    def precision(self):
      """Renvoie la precision de l'environnement"""
      self._precision

    @property
    def robotX(self):
       """Renvoie les coordonnées x du robot de  l'environnement"""
       return self._robot.x
    
    @property
    def robotY(self):
       """Renvoie les coordonnées y du robot de  l'environnement"""
       return self._robot.y
    
    @property
    def robotRayon(self):
      return self._robot.rayon
    
    def addObstacle(self,x,y,h,d,rayon):
        """Créer et dépose l'obstacle s'il n'y a pas déjà un objet dans la case avec les mêmes coordonnées en faisant appel à la fonction estObstacle
        :param x: Coordonnées x de l'obstacle qu'on va créer
        :param y: Coordonnées y de l'obstacle qu'on va créer
        :param h: hauteur de l'obstacle
        :param d: distance du sol de l'obstacle
        """
        if not (self.estObstacle(x,y,rayon) and self.estMur(x,y,rayon) and self.estRobot):
            self._ensemble_obstacles.add(Obstacle(x,y,h,d,rayon))
        return
    
    def detectCollision(self):
        '''
        Detecte si il y a une collision (un crash) entre le robot et un obstacle avec une precision
        '''
        for obs in self._ensemble_obstacles:
           dist=calculDistance(self._robot,obs)
           if(dist - self.robotRayon - obs.rayon <= self._precision):  #verifie si la distance entre les 2 objets est inferieure a la somme des rayons
              return True
        return False
    
def calculDistance(objet1, objet2):
    '''
    Calcule la distance entre le centre de deux objets passer en paramètre. Les objets peuvent être des robots ou des obstacles.
    :param objet1 : robot/obstacle
    :param objet2 : robot/obstacle
    :return : valeur négative ou égale à 0 si les objects sont en collision (ne gère pas la hauteur)
    :return : sinon valeur positive correspondant à la distance en valeur absolue la plus petite entre les 2 rayons (distance générale, ne pdonne pas la direction)
    '''

    return math.sqrt(math.pow(objet1.x-objet2.x,2)+ math.pow(objet1.y-objet2.y,2))



       

