class Robot:

  def __init__(self,vitesse ):
    '''Constructeur de la classe Robot,avec des coordonnées par défaut (0,0) et une orientation=0 (par défaut) 
    (angle en radian) et une vitesse en forme d'un vecteur
    :param vitesse: liste de 2 élements [vx,vy] qui représente le vecteur de la vitesse du robot'''
    self.x = 0.0
    self.y = 0.0
    self.orientation=0
    self.vitesse=vitesse
  
