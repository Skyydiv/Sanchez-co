import math
class Robot:
  WHEEL_BASE_WIDTH         = 117  # distance (mm) de la roue gauche a la roue droite.
  WHEEL_DIAMETER           = 66.5 #  diametre de la roue (mm)
  WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
  WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi # perimetre de la roue (mm)
  
  def __init__(self, vitesseRoueGauche, vitesseRoueDroite, rayon):
    '''Constructeur de la classe Robot,représentation sous forme de cercle avec des coordonnées par défaut le coin haut gauche (rayon+0.1, rayon+0.1) , vitesse de la roue gauche et droite, un rayon une orientation (angle en radian), une vitesse max et min
    :param vitesseRoueGauche: vitesse de la roue gauche du robot
    :param vitesseRoueDroite: vitesse de la roue droite du robot
    :param rayon: rayon de l'objet (en mm)
    '''
    self.x =0.1+rayon #pour être dans l'env
    self.y = 0.1+rayon
    self.rayon = rayon
    self.orientation=0
    self.vitesseRoueDroite=vitesseRoueDroite
    self.vitesseRoueGauche=vitesseRoueGauche

  def setVitesse(self, vRoueGauche, vRoueDroite):
    """Set la vitesse des roues"""
    self.vitesseRoueDroite=vRoueDroite
    self.vitesseRoueGauche=vRoueGauche

  def deplacer(self,delta_t):
    """
    Change les coordonnées x et y du robot selon sa vitesse et son angle avec un pas de temps
    """
    self.x +=(self.vitesseRoueGauche+self.vitesseRoueDroite)/2 * math.cos(self.orientation)*delta_t #vitesse linéare moyenne du robot
    self.y +=(self.vitesseRoueGauche+self.vitesseRoueDroite)/2 * math.sin(self.orientation)*delta_t

  def distanceParcourue(self,delta_t):
    old_x=self.x
    old_y=self.y
    self.deplacer(self,delta_t)
    return math.sqrt(abs(self.x-old_x)^2+abs(self.y-old_y)^2)


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
  
