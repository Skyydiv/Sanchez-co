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
    :param env: l'environnement dans lequel se trouve le robot
    :param n: le nombre de case à avancer
    '''
    if (self.orientation=="bas"):
      newY=self.y+n
      if (self.VerifieMur(n,env)):
        print("Le robot ne peut pas avancer")
      else:
        env.tab[self.x][self.y]=None
        self.y=newY
        self.deposer(env,self.x,newY)
    if (self.orientation=="haut"):
      newY=self.y-n
      if (self.VerifieMur(n,env)):
        print("Le robot ne peut pas avancer")
      else:
        env.tab[self.x][self.y]=None
        self.y=newY
        self.deposer(env,self.x,newY)
    if (self.orientation=="droite"):
      newX=self.x+n
      if (self.VerifieMur(n,env)):
        print("Le robot ne peut pas avancer")
      else:
        env.tab[self.x][self.y]=None
        self.x=newX
        self.deposer(env,newX,self.y)
    if (self.orientation=="gauche"):
      newX=self.x-n
      if (self.VerifieMur(n,env)):
        print("Le robot ne peut pas avancer")
      else:
        env.tab[self.x][self.y]=None
        self.x=newX
        self.deposer(env,newX,self.y)

    
  def VerifieMur(self,a,env):
    '''Verfie si quand le robot avance de a il ya un mur
    :param a:le nombre de case que va parcourir le robot 
    '''
    if ((self.orientation=="droite")and((self.x+a)>=env.nblignes)):
      print("Attention il ya un mur!!")
      return True
    elif ((self.orientation=="gauche")and((self.x-a)<0)):
      print("Attention il ya un mur!!")
      return True
    elif ((self.orientation=="haut")and((self.y-a)<0)):
      print("Attention il ya un mur!!")
      return True
    elif ((self.orientation=="bas")and((self.y+a)>=env.nblignes)):
       print("Attention il ya un mur!!")
       return True
    else:
      print("Le robot peut avancer")
      return False
  


  
#tests
robot1=Robot("droite")
print(robot1.x)
print(robot1.y)
