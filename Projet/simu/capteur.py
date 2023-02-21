import math

def intersectionDroites(a1, b1, c1, a2, b2, c2):
    """
    Calcule les coordonnées cartésiennes de l'intersection de deux droites à partir de leurs équations, sous la forme ax + by + c = 0.
    :param a1 (float): Coefficient a de la première droite.
    :param b1 (float): Coefficient b de la première droite.
    :param c1 (float): Coefficient c de la première droite.
    :param a2 (float): Coefficient a de la deuxième droite.
    :param b2 (float): Coefficient b de la deuxième droite.
    :param c2 (float): Coefficient c de la deuxième droite.
    :return: Les coordonnées cartésiennes (x, y) de l'intersection des deux droites.
    """

    # Les droites sont parallèles, pas d'intersection.
    if a1*b2 - a2*b1 == 0:
        return None
    else:
        # Calcul des coordonnées de l'intersection.
        x = (b1*c2 - b2*c1) / (a1*b2 - a2*b1)
        y = (a2*c1 - a1*c2) / (a1*b2 - a2*b1)
        return (x, y)


def intersectionDroiteCercle(a, b, c, h, k, r):
    """
    Calcule les coordonnées cartésiennes des intersections entre une droite et un cercle.

    La droite est représentée par son équation sous la forme ax + by + c = 0.
    Le cercle est représenté par son centre (h, k) et son rayon r.

    Args:
        a (float): Coefficient a de l'équation de la droite.
        b (float): Coefficient b de l'équation de la droite.
        c (float): Coefficient c de l'équation de la droite.
        h (float): Coordonnée x du centre du cercle.
        k (float): Coordonnée y du centre du cercle.
        r (float): Rayon du cercle.

    Returns:
        list: Liste contenant les coordonnées cartésiennes des points d'intersection entre la droite et le cercle.
    """
    # Calcul des coefficients de l'équation réduite de la droite ax + by + c = 0
    # sous la forme y = mx + p
    m = -a / b
    p = -c / b

    # Calcul des coordonnées x des points d'intersection
    A = 1 + m**2
    B = 2*m*p - 2*h - 2*k*m
    C = h**2 + k**2 + p**2 - 2*k*p - r**2
    delta = B**2 - 4*A*C

    # Vérification de la présence de solutions réelles
    if delta < 0:
        return []

    x1 = (-B + math.sqrt(delta)) / (2*A)
    x2 = (-B - math.sqrt(delta)) / (2*A)

    # Calcul des coordonnées y correspondantes
    y1 = m * x1 + p
    y2 = m * x2 + p

    # Renvoi des coordonnées des points d'intersection sous forme de liste
    return [(round(x1,1), round(y1,1)), (round(x2,1), round(y2,1))]


def equationDroitePolaire(vect):
    """
    Convertit un vecteur donné en coordonnées polaires en une équation de droite de vecteur directeur sous la forme ax+by+c=0.
    :param vect (tuple): Un tuple (r, theta) représentant le vecteur en coordonnées polaires.
    :return Un tuple (a, b, c) représentant l'équation de la droite de vecteur directeur.
    """
    r, theta = vect
    # Calcul des coefficients de la droite
    m = - math.tan(theta)
    p = r * math.sin(theta)

    # Conversion de l'équation de la droite sous la forme ax + by + c = 0
    a = m
    b = 1
    c = -p
    return (a, b, c)

def dist(c1,c2):
    """
    Renvoie la distance entre les 2 points
    :arg c1(tuple): (x1,y1)
    :arg c2(tuple): (x2,y2)
    :return d (float): distance
    """
    x1, y1 = c1
    x2, y2 = c2
    return math.sqrt( math.pow(x2-x1,2)+ math.pow(y2-y1,2) )

def plusProche(c,liste):
    """
    Cherche le point le plus proche des coordonnés donnés en parametre dans une liste de couple de coordonnés
    :arg c (tuple): coordonné (x,y)
    :arg liste (liste:tuple) : liste de coordonnés [(x1,y1),(x2,y2),...]
    :return cMin : telle cMin les coordonnées les plus proche de c 
    """

    min=liste[0]
    distMin=math.inf

    for e in liste:
        dTmp=dist(c,e)
        if dTmp<distMin:
            min=e
            distMin=dTmp

    return min











class Capteur:
    def __init__(self, angle):
        self.angle = angle

    def checkObstacle(self,env):
        '''
        Vérifie si il y a un obstacle présent devant le robot.
        :param env: L'environnement 
        :param tailleRayon (float): l'épaisseur sur laquelle le rayon détect (sa précision)
        '''
        r = env.robot #récupère le robot

        rA,rB,rC = equationDroitePolaire((1,r.orientation)) #calcul l'équation de la droite à partir des info du robot
        lObstacle=[]    #liste de tout les obstacles rencontré, le 1 er fais partie de ceux là

        for o in env.ensemble_obstacles: #parcourt tout les obstacles de l'environnement

            if o.x >= r.x - r.rayon -o.rayon: #on regarde que les obstacles devant le robot
                lInter=intersectionDroiteCercle(rA,rB,rC,o.x,o.y,o.rayon) #Donne la liste des coordonnées d'intersection entre le rayon du robot et le cercle
                if lInter!=[]:
                    proche=plusProche((r.x,r.y), lInter) #récupère le plus proche 
                    lObstacle.append(proche) 
            
        if lObstacle==[]: #si aucun obstacle rencontré 
            return None
        first=plusProche((r.x,r.y),lObstacle)
        return env.calculDistance(r,first)

 
     
    def capteur_distance(self,env):
        """Renvoie la distance à l'obstacle le plus près du robot dans sa direction si il y en a un, sinon renvoie la distance au mur dans sa direction.
        :param env: L'environnement
        :return : distance obstacle/mur le plus proche
        """
        
        checkO = self.checkObstacle(env)
        return checkO

    # if checkO != None:
    #     return check0
        
    # eqMurD= (-1,0,env.coordsmax[0])
    # eqMurG = (-1,0,0)
    #  eqMurH = (0,-1,0)
    #  eqMurB = (0,-1,env.coordsmax[1])

    # lM=[eqMurD,eqMurG,eqMurH,eqMurB]