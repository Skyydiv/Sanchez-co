import math
from time import sleep
from time import time
from threading import Thread
from .proxy import ControleurRobotVirtuel

class BoucleIA(Thread):
    """ 
    Classe qui permet de lancer une boucle d'IA
    """
    
    def __init__(self, controleur, ia,delta_t):
        """
        Constructeur de la classe.

        Paramètres :
        - controleur : Objet controleur
        - ia : Objet IA
        - delta_t : Intervalle de temps
        """
        Thread.__init__(self)
        self.controleur = controleur
        self.ia=ia
        self.delta_t=delta_t


    def run(self):
        """
        Méthode exécutée lorsque la boucle d'intelligence artificielle démarre.
        """
        self.ia.start()
        self.controleur.reset_time()
        while self.ia.en_cours:
            self.ia.update()
            sleep(self.delta_t)

class Ia_Avancer_tout_droit:
    """ 
    sous classe de IA qui permet d'avancer tout droit
    """
    
    def __init__(self, distance, v, controleur):
        """
        Constructeur de la classe.

        Paramètres :
        - distance : Distance à parcourir
        - v : Vitesse de déplacement
        - controleur : Objet controleur
        """
        
        self.goal = distance
        self.v = v
        self.en_cours=False
        self.CR=controleur
       
        
    def start(self):
        """
        Démarre l'IA pour avancer tout droit.
        """
        self.CR.reset()
        self.en_cours=True
        self.CR.avancerToutDroit(self.v)
       
 
    def stop(self):
         """
        Vérifie si l'IA doit s'arrêter.

        Retourne :
        - True si l'une des roues a parcouru plus que la distance à parcourir, sinon False.
        """
        
        return self.CR.distanceParcourue >= self.goal
    
    
    def update(self):
         """
        Met à jour l'IA pour avancer tout droit.

        Si la condition d'arrêt est vérifiée, arrête le robot et réinitialise la distance parcourue.
        Sinon, met à jour le contrôleur et continue d'avancer tout droit.
        """
        if self.stop():
            self.en_cours=False
            self.CR.stop()
            self.CR.resetDistanceParcourue()
            
        else:
            self.CR.update()
            self.CR.avancerToutDroit(self.v)
    
          
    
class IATournerAngle:
    """
    Classe IA pour tourner d'un certain angle
    """
    def __init__(self, controleur, angle, vitesse):
        """
        Constructeur de la classe.

        Paramètres :
        - controleur : Objet controleur
        - angle : Angle à tourner (en degrés)
        - vitesse : Vitesse de rotation
        """
        
        self.angle = math.radians(angle) 
        #on convertit les degrés passés en paramètre en radians pour les calculs
        self.CR=controleur
        self.en_cours=False
        self.v=vitesse

    def start(self):
        """
        Démarre l'IA pour tourner.
        """
        self.CR.reset()
        self.en_cours=True
        self.CR.tournerDroite(self.v)
        
    def stop(self):
         """
        Vérifie si l'IA doit s'arrêter.

        Retourne :
        - True si l'angle parcouru est supérieur ou égal à la valeur absolue de l'angle cible, sinon False.
        """
        
        return self.CR.angleParcouru > abs(self.angle) 
        
    def update(self):
        """
        Met à jour l'IA pour tourner à droite.

        Si la condition d'arrêt est vérifiée, arrête le robot et réinitialise l'angle parcouru.
        Sinon, met à jour le contrôleur et continue de tourner à droite.
        """
        if self.stop():
            self.en_cours=False
            self.CR.stop()
            self.CR.resetAngleParcourue()

        else:
            self.CR.update()
            self.CR.tournerDroite(self.v)
            
   
        
        
        
class IAseq:
         """
            sous classe d'IA permettant de lancer une liste d'IA à la suite
         """
        
        def __init__(self,controleur,liste):
        """
        Constructeur de la classe.

        Paramètres :
        - controleur : Objet controleur
        - liste : Liste d'objets IA
        """
            self.CR=controleur
            self.ia_list=liste
            self.en_cours=False
            self.ia_en_cours=0
            
        def start(self):
        """
        Démarre l'exécution de la séquence d'IA.
        """
            self.en_cours=True
            self.ia_list[self.ia_en_cours].start()
            
        def stop(self):
        """
        Vérifie si la séquence d'IA doit s'arrêter.

        Retourne :
        - True si toutes les IA de la séquence ont terminé, sinon False.
        """
            if not (self.ia_list[self.ia_en_cours].en_cours):
                self.ia_en_cours+=1
                if self.ia_en_cours>=len(self.ia_list):
                    self.en_cours=False
                    return True
                else:
                    self.ia_list[self.ia_en_cours].start()
                    return False
            return False
        
        def update(self):
        """
        Met à jour la séquence d'IA.

        Si la séquence doit s'arrêter, arrête le contrôleur et réinitialise l'index de l'IA en cours.
        Sinon, met à jour l'IA en cours.
        """
            if self.stop():
                self.CR.stop()
                self.en_cours=False
                self.ia_en_cours=0
                
            else:
                self.ia_list[self.ia_en_cours].update()


class IAIfThenElse:
    """
    sous classe d'IA évaluant une condition et ne faisant rien si elle est fausse
    """
    def __init__(self, controleur, condition, ia_then, ia_else):
    
        self.CR = controleur
        self.condition = condition
        self.ia_then = ia_then
        self.ia_else = ia_else
        self.en_cours = False

    def start(self):
         """
        Méthode exécutée lorsque la boucle d'intelligence artificielle démarre.
        """
        self.en_cours = True

    def update(self, delta_t):
        if not self.en_cours:
            return

        if self.condition():
            print("Condition vraie - ia_then")
            if self.ia_else and self.ia_else.en_cours:
                self.ia_else.stop()
            if not self.ia_then.en_cours:
                self.ia_then.start()
            self.ia_then.update(delta_t)
        else:
            print("Condition fausse - ia_else")
            if self.ia_then.en_cours:
                self.ia_then.stop()
            if self.ia_else and not self.ia_else.en_cours:
                self.ia_else.start()
            if self.ia_else:
                self.ia_else.update(delta_t)

    def stop(self):
        if (self.ia_then and self.ia_then.en_cours):
            return self.ia_then.stop()
        if (self.ia_else and self.ia_else.en_cours):
            return self.ia_else.stop()

            


def TracerCarre(controleur,distance,vitesse):
    """
    strategie de base pour tracer un carre
    """

#ia pour avancer tout droit 
    ia10=Ia_Avancer_tout_droit(distance,vitesse,controleur)
    
#ia pour tourner 
    iaa=IATournerAngle(controleur,90,vitesse)
    
#ia seq
    iacarre=IAseq(controleur,[ia10,iaa,ia10,iaa,ia10,iaa,ia10,iaa])

    return iacarre
