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
    self.rayon = rayon
    self.orientation=0

    self.WHEEL_BASE_WIDTH=117 # distance (mm) de la roue gauche a la roue droite.
    self.WHEEL_DIAMETER=66.5 # diametre de la roue (mm)
    self.WHEEL_BASE_CIRCUMFERENCE =self.WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
    self.WHEEL_CIRCUMFERENCE = self.WHEEL_DIAMETER * math.pi # perimetre de la roue (mm)


    self.MOTOR_LEFT=None
    self.MOTOR_RIGHT=None


    self.vitesseRoueDroite=0
    self.vitesseRoueGauche=0

    
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


  def deplacer(self):
    """Deplace le robot en fonction de la vitesse des roues"""

    #Calcul des vitesses lineire et angulaire
    v=(self.vitesseRoueGauche + self.vitesseRoueDroite) / 2 #vitesse lineaire
    w=(self.vitesseRoueDroite - self.vitesseRoueGauche) / self.WHEEL_BASE_WIDTH #vitesse angulaire

    wheel_parameter= self.WHEEL_DIAMETER/2

    #set vitesse des roues
    self.vitesseRoueGauche = (v - (w * self.WHEEL_BASE_WIDTH)) / wheel_parameter #calcul vitesseRoueGauche
    self.vitesseRoueDroite = (v + (w * self.WHEEL_BASE_WIDTH)) / wheel_parameter #calcul vitesseRoueGauche

    #set vitesse des moteurs 
    self.set_motor_dps(self.MOTOR_RIGHT,self.vitesseRoueDroite)
    self.set_motor_dps(self.MOTOR_LEFT,self.vitesseRoueGauche)

    #update les coord du robot
    self.UpdatePosition(v, w, delta_t=1/1000)

    time.sleep(1/1000)
     
  

  def UpdatePosition(self, v, w, delta_t):
    """
    Change les coordonnées x et y du robot selon sa vitesse et son angle avec un pas de temps
    :param v: vitesse linaire
    :param w: vitesse angualire
    :param delta_t : pas de temps
    """

    self.orientation += w * delta_t 
        
    self.x += v * math.cos(self.orientation) * delta_t 
    self.y += v * math.sin(self.orientation) * delta_t
    


  def distanceParcourue(self,delta_t):
    """Distance parcourue après un déplacement du robot"""
    old_x=self.x
    old_y=self.y
    self.deplacer(self,delta_t)
    return math.sqrt(abs(self.x-old_x)^2+abs(self.y-old_y)^2)

  def get_motor_position(self):
    """Retourne un couple de couple de position des roues du robot grâce à la distance des deux roues et à l'orientation et position du robot"""
    return ((self.x-self.WHEEL_BASE_WIDTH/2*math.sin(self.orientation),self.y+self.WHEEL_BASE_WIDTH/2*math.cos(self.orientation)),(self.x+self.WHEEL_BASE_WIDTH/2*math.sin(self.orientation),self.y-self.WHEEL_BASE_WIDTH/2*math.cos(self.orientation)))



  
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
  
