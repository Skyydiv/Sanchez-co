class Robot:

  def __init__(self,vitesse, rayon, angle=0):
    '''Constructeur de la classe Robot,représentation sous forme de cercle avec des coordonnées par défaut (0.1,0.1), une vitesse en forme d'un vecteur, un rayon une orientation (angle en radiant)
    :param vitesse: liste de 2 élements [vx,vy] qui représente le vecteur de la vitesse du robot
    :param rayon: rayon de l'objet (en cm)
    :param orientation(optionel): angle (en radian) (par défaut, orientation=0) 
    '''
    self.x = rayon + 0.1 #pour être dans l'env
    self.y = rayon + 0.1
    self.rayon = rayon
    self.orientation=angle
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
  
