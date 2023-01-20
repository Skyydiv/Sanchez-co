class Objet:

  def __init__(self, orientation):
    '''Constructeur de la classe Robot, créer un robot dans un environnement avec des coordonnées par défaut (0,0) et une orientation
    :param environnement: Environnement dans lequel le robot sera placé
    :param orientation: Orientation du robot'''
    self.x = 0
    self.y = 0
    self.orientation=orientation

robot1=Objet("coucou", "bas")

print(robot1.x)
print(robot1.y)
