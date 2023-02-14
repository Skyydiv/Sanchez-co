class Wheel:
    def __init__(self, rayon):
        self.rayon = rayon

    def vitesse_angulaire(self, vitesse):
        return vitesse / self.rayon