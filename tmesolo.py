#Question 1.1
def addObstacle4coins(self,rayon):
   '''Depose un obstacle aux 4 coins de l'environnemente
    :param rayon: rayon de l'obstacle
    '''
    self._environnement.addObstacle(0+rayon,0+rayon,0,0,rayon)
    self._environnement.addObstacle(0+rayon,self.coordsYmax+rayon,0,0,rayon)
    self._environnement.addObstacle(self.coordsXmax-rayon,0+rayon,0,0,rayon)
    self._environnement.addObstacle(self.coordsXmax-rayon,self.coordsYmax-rayon,0,0,rayon)

#Question 1.2
def drawObstacles(self):
    '''dessine l'ensemble des obstacles'''
    for obs in self.obstacles:
        x=obs.x
        y=obs.y
        r=obs.rayon
        self.canv.create_oval(x-r,y-r,x+r,y+r, fill='#FFA500')

#Question 1.3
class View:
    def drawRobot(self):
        '''dessine le Robot'''
        x=self.robot.x
        y=self.robot.y
        r=self.robot.rayon
        o=degrees(self.robot.orientation)
        self.canv.create_arc(x-r,y-r,x+r,y+r, start=45-o, extent=270,fill="yellow")
        if self.robot.lever==False:
            self.robot_trajet.append((x, y))
        
    def drawRobotTrajet(self):
        '''dessine le trajet du robot'''
        if len(self.robot_trajet) > 1:
            self.canv.create_line(self.robot_trajet, fill='white')

class Controleur:
    def dessine(self, b: bool):
        """dessine le trajet le robot lorsqu'il est abaissé"""
        self.robot.setlever(b)

#Question 1.4

#Question 2.1

def dessineRectangle(controleur, distance, vitesse):
    controleur.dessine(False)
    ia1=Ia_Avancer_tout_droit(distance,vitesse,controleur)
    ia2=Ia_Avancer_tout_droit(2*distance,vitesse,controleur)
    iaa=IATournerAngle(controleur,90,vitesse)
    rectangle=IAseq(controleur, [ia1,iaa,ia2,iaa,ia1,iaa,ia2,iaa])
    return rectangle

#Question 2.2

def dessineRectangleDroite(controleur, distance, vitesse):
    controleur.dessine(False)
    ia1=dessineRectangle(controleur, distance, vitesse)
    ia2=dessineDroite(controleur, 2 * distance, vitesse)
    ia=Ia_Avancer_tout_droit(2*distance,vitesse,controleur)
    motif = IAseq(controleur, [ia1, ia, ia2])
    return motif

#Question 3.1

class Robot:
    def __init__(self,rayon):
        '''Constructeur de la classe Robot,représentation sous forme de cercle avec des coordonnées par défaut le coin haut gauche (rayon+0.1, rayon+0.1) 
        :param rayon: rayon de l'objet (en mm)
        '''
        self.rayon = rayon
        self._lever=True
        self._capteur=Capteur(self.x+rayon, self.y, 5)

        self._x=100.1+rayon #coordonnées x du robot
        self._y=100.1+rayon #coordonnées y du robot

        self._orientation=0 #(radians)
        self.capteur=Capteur(0) #Capteur du robot


        #self.MOTOR_LEFT_Offset=0
        #self.MOTOR_RIGHT_Offset=0

        self.vitesseRoueDroite=0 #degre par sec
        self.vitesseRoueGauche=0 #degre par sec

        self._distance_parcourue_roue_gauche=0 #en mm
        self._distance_parcourue_roue_droite=0 #en mm

        self._angle_parcouru=0 #(en degre)

class Emetteur:
  """Classe représentant un émetteur"""
  def __init__(self,x, y,rayon):
    self._x=x
    self._y=y
    self._rayon=rayon

  @property
  def x(self):
    """Renvoie coordonnées x du robot"""
    return self._x
  
  @property
  def y(self):
    """Renvoie coordonnées y du robot"""
    return self._y
  
  @property
  def rayon(self):
    """Renvoie le rayon du capteur"""
    return self._rayon
     
class Capteur:
  """Classe représentant un capteur"""
  def __init__(self,x, y,rayon):
    self._x=x
    self._y=y
    self._rayon=rayon

  @property
  def x(self):
    """Renvoie coordonnées x du robot"""
    return self._x
  
  @property
  def y(self):
    """Renvoie coordonnées y du robot"""
    return self._y

  @property
  def rayon(self):
    """Renvoie le rayon du capteur"""
    return self._rayon

#Question 3.2

