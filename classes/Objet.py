class Robot:

  def __init__(self,vitesse):
    '''Constructeur de la classe Robot,avec des coordonnées par défaut (0,0) et une orientation=0 (par défaut) 
    (angle en radian) et une vitesse en forme d'un vecteur
    :param vitesse: liste de 2 élements [vx,vy] qui représente le vecteur de la vitesse du robot'''
    self.x = 0.1
    self.y = 0.1
    self.orientation=0
    self.vitesse=vitesse

class Obstacle :
  '''Obstacle qui peuvent être présent dans l'environnement'''
    
  def __init__(self,x,y,h,d):
      '''Construteur de l'objet Obstacle qui initialise les coordonnées,l'hauteur, et la distance du sol
      :param x: coordonnée des abscisses
      :param y: coordonnée des ordonnées
      :param h: hauteur de l'obstacle
      :paran d: distance du sol
      '''
      self.x=x
      self.y=y
      self.hauteur=h
      self.distSol=d
  
