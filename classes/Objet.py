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
  
  def avancer(self, env, n):
    '''Fais avancer le robot de n cases dans env si possible, renvoie un message sinon
    :param n: le nombre de case à avancer
    '''
    if (self.orientation=="bas"):
      newY=self.y-n
      if (newY>=env.nblignes):
        print("Le robot ne peut pas avancer")
      if (estMur(x,newY)):
        print("Le robot ne peut pas avancer")
      else:
        env.tab[self.x][self.y]=None
        self.y=newY
        deposer(env,x,newY)
    if (self.orientation=="haut"):
      newY=self.y+n
      if (newY<0):
        print("Le robot ne peut pas avancer")
      if (estMur(x,newY)):
        print("Le robot ne peut pas avancer")
      else:
        env.tab[self.x][self.y]=None
        self.y=newY
        deposer(env,x,newY)
    if (self.orientation=="droite"):
      newX=self.x+n
      if (newX>=env.nbcolonnes):
        print("Le robot ne peut pas avancer")
      if (estMur(newX,y)):
        print("Le robot ne peut pas avancer")
      else:
        env.tab[self.x][self.y]=None
        self.x=newX
        deposer(env,newX,y)
    if (self.orientation=="gauche"):
      newX=self.x-n
      if (newX<0):
        print("Le robot ne peut pas avancer")
      if (estMur(newX,y)):
        print("Le robot ne peut pas avancer")
      else:
        env.tab[self.x][self.y]=None
        self.x=newX
        deposer(env,newX,y)


  
#tests
robot1=Robot("droite")
print(robot1.x)
print(robot1.y)
