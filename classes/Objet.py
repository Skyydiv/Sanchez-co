from math import cos, sin, sqrt
class Robot:

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
    self.distanceRoues=117 #donné dans l'API du robot
    self.vitesseMax=50
    self.vitesseMin=0

  def setVitesseRoueGauche(self,vg):
    """Modifie la vitesse de la roue gauche
    :param vg: nouvelle vitesse de la roue gauche
    """
    if (vg<self.vitesseMin or vg>self.vitesseMax):
      raise ValueError("La vitesse doit être supérieur ou égal à vitesseMin et inférieur à vitesseMax.")
    self.vitesseRoueGauche=vg

  def setVitesseRoueDroite(self,vd):
    """Modifie la vitesse de la roue droite
    :param vd: nouvelle vitesse de la roue droite
    """
    if (vd<self.vitesseMin or vd>self.vitesseMax):
      raise ValueError("La vitesse doit être supérieur ou égal à vitesseMin et inférieur à vitesseMax.")
    self.vitesseRoueDroite=vd

  def tournerDroite(self):
    """Arrête la roue droite pour tourner à droite"""
    self.setVitesseRoueDroite(0)

  def tournerGauche(self):
    """Arrête la roue gauche pour tourner à gauche"""
    self.setVitesseRoueGauche(0)

  def arret(self):
    """ Arrête le robot en mettant la vitesse de ses deux roues à 0 """
    self.vitesseRoueDroite=0
    self.vitesseRoueGauche=0

  def changerVitesse(self, vRoueGauche, vRoueDroite):
    """Set la vitesse des roues"""
    self.vitesseRoueDroite=vRoueDroite
    self.vitesseRoueGauche=vRoueGauche

  def deplacer(self):
    """
    Change les coordonnées x et y du robot selon sa vitesse et son angle avec un pas de temps
    """
    self.x +=(self.vitesseRoueGauche+self.vitesseRoueDroite)/2 #vitesse linéare moyenne du robot
    self.y +=(self.vitesseRoueGauche+self.vitesseRoueDroite)/2 


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
  
