import math
import Roue
import time

class Robot:

  
  def __init__(self, rayon):
    '''Constructeur de la classe Robot,représentation sous forme de cercle avec des coordonnées par défaut le coin haut gauche (rayon+0.1, rayon+0.1) 
    :param rayon: rayon de l'objet (en mm)
    '''
    self.x =0.1+rayon #pour être dans l'env
    self.y = 0.1+rayon
    self.rayon = rayon #(mm)
    self.orientation=0 #(radians)

    self.WHEEL_BASE_WIDTH=117 # distance (mm) de la roue gauche a la roue droite.
    self.WHEEL_DIAMETER=66.5 # diametre de la roue (mm)
    self.WHEEL_BASE_CIRCUMFERENCE =self.WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
    self.WHEEL_CIRCUMFERENCE = self.WHEEL_DIAMETER * math.pi # perimetre de la roue (mm)


    self.MOTOR_LEFT=None
    self.MOTOR_RIGHT=None

    self.MOTOR_LEFT_Offset=0
    self.MOTOR_RIGHT_Offset=0

    self.vitesseRoueDroite=4
    self.vitesseRoueGauche=3

    self.v=(self.vitesseRoueGauche + self.vitesseRoueDroite) / 2 #vitesse lineaire
    self.w=(self.vitesseRoueDroite - self.vitesseRoueGauche) / self.WHEEL_BASE_WIDTH #vitesse angulaire

    # self.roueGauche=Roue(self.WHEEL_BASE_WIDTH/2)
    # self.roueDroite=Roue(self.WHEEL_BASE_WIDTH/2)

    # self.vitesseAngulaireDroite=self.roueDroite.vitesse_angulaire(vitesseRoueDroite)
    # self.vitesseAngulaireGauche=self.roueGauche.vitesse_angulaire(vitesseRoueGauche)

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

  def deplacer(self, intervalle_temps):
        """deplace le robot dans un intervalle de temps
        :param intervalle_temps: intervalle de temps dans lequel le robot avance"""
        self.vitesseRoueDroite = self.v + self.w * self.WHEEL_BASE_WIDTH / 2
        self.vitesseRoueGauche = self.v - self.w * self.WHEEL_BASE_WIDTH / 2

        distance_parcourue_droite = self.vitesseRoueDroite* intervalle_temps
        distance_parcourue_gauche = self.vitesseRoueGauche * intervalle_temps

        newOrientation = (distance_parcourue_droite - distance_parcourue_gauche) / self.WHEEL_BASE_WIDTH
        self.orientation += newOrientation

        newV = (distance_parcourue_droite + distance_parcourue_gauche) / 2 #recalcul vitesse lineare
        self.x += newV * math.cos(self.orientation)
        self.y += newV * math.sin(self.orientation)

  def setVitesse(self,Vr,Vg):
    """set la vitesse des roues
    :param Vr : vitesse de la roue droite
    :param Vg : vitesse de la roue gauche"""
    self.vitesseRoueDroite=Vr
    self.vitesseRoueGauche=Vg

  def get_motor_position(self):
    """Retourne un couple de couple de position des roues du robot grâce à la distance des deux roues et à l'orientation et position du robot"""
    return ((self.x-self.WHEEL_BASE_WIDTH/2*math.sin(self.orientation),self.y+self.WHEEL_BASE_WIDTH/2*math.cos(self.orientation)),(self.x+self.WHEEL_BASE_WIDTH/2*math.sin(self.orientation),self.y-self.WHEEL_BASE_WIDTH/2*math.cos(self.orientation)))

   
  def offset_motor_encoder(self, port, offset):
    """
    Fixe l'offset des moteurs (en degres)   
    :port: un des deux moteurs MOTOR_LEFT ou MOTOR_RIGHT (ou les deux avec +)
    :offset: l'offset de decalage en degre.
    """
    if(port==self.MOTOR_RIGHT):
      self.MOTOR_RIGHT_Offset=offset
    if(port==self.MOTOR_LEFT):
      self.MOTOR_LEFT_Offset=offset
  
  # def distanceParcourue(self,delta_t):
  #   """Distance parcourue après un déplacement du robot"""
  #   old_x=self.x
  #   old_y=self.y
  #   self.deplacer(self,delta_t)
  #   return math.sqrt(abs(self.x-old_x)^2+abs(self.y-old_y)^2)

  
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
  
