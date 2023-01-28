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