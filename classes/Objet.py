class Robot:

  def __init__(self, orientation):
    '''Constructeur de la classe Robot,avec des coordonnées par défaut (0,0) et une orientation
    :param orientation: Orientation du robot'''
    self.x = 0
    self.y = 0
    self.orientation=orientation
  
  def deposer(self,env,x,y):
      '''Depose le robot dans l'environnement aux cooordonnées (x,y)
        
      :param env: environnement dans lequel se trouve le robot
      :param x: ligne dans laquelle on dépose le Robot
      :param y: colonne dans laquelle on dépose le Robot
      '''
      env.tab[x][y]=self
      print("Le robot a été déposé dans l'environnement")
      self.x=x
      self.y=y

  def getPos(self):
    '''Renvoie et affiche les coordonnées du robot'''
    print("Le robot se trouve dans la case (",self.x,",",self.y,")")
    return (self.x,self.y)

  def tourner(self,orientation) :
    '''Change la direction du robot
    :param direction: la nouvelle direction vers laquelle le robot tourne
    '''
    if(self.orientation!=orientation):
          self.orientation=orientation

  
#tests
robot1=Robot("droite")
print(robot1.x)
print(robot1.y)
