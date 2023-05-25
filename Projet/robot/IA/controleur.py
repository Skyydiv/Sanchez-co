import math 
import time

class Controleur:
    def __init__(self, robot):
        self.robot=robot
        self.deb=0
        self.fin=0
        self.temps_total=0
        self._distanceParcourue=0
        self._angleParcouru=0 #en radians

    def setVitesseRoues(self, vitesseg, vitessed):
        """
        :param vitesseg: vitesse de la roue gauche
        :param vitessed: vitesse de la roue droite
        """
        self.set_Vitesse(vitesseg, vitessed)
    
    def avancerToutDroit(self, v):
        """
        :param v: vitesse de la roue gauche et droite
        """
        self.set_Vitesse(v,v)

    def tournerDroite(self,v):
        """
        :param v: vitesse de rotation
        """
        self.set_Vitesse(v,-v)
    
    def tournerGauche(self,v):
        """
        :param v: vitesse de rotation
        """
        self.set_Vitesse(-v,v)

    def stop(self):
        """
        arrete le robot
        """
        self.robot.stop()

    def update(self):
        """
        update les distances et l'angle parcouru depuis le dernier appel de update
        """
        self.fin=time.time()
        self.temps_total=self.fin-self.deb
        self.deb=self.fin

        self.calculDistanceParcourue()
        self.calculAngleParcouru()

    def reset_time(self):
        """
        remet le temps a 0
        """
        self.deb=time.time()
        self.temps_total=0

    @property
    def distanceParcourue(self):
        """
        :return : la distance parcourue par le robot depuis la derniere remise a 0
        """
        return self._distanceParcourue
    
    @property
    def angleParcouru(self):
        """
        :return : l'angle parcouru par le robot depuis la derniere remise a 0
        """
        return self._angleParcouru
     
    def resetDistanceParcourue(self):
        """
        remet la distance parcourue a 0
        """
        self._distanceParcourue=0

    def resetAngleParcourue(self):
        """
        remet l'angle parcouru a 0
        """
        self._angleParcouru=0


class ControleurRobotVirtuel(Controleur):
    """
    classe controleur pour le robot virtuel
    """
    def __init__(self, robot):
        Controleur.__init__(self,robot)

    def set_Vitesse(self,vitesseg, vitessed):
        self.robot.setVitesse(vitesseg,vitessed)
        
    def calculDistanceParcourue(self):
        """
        :param delta_t: un intervalle de temps 
        :return: la distance parcourue par le robot pour delta_t et met a jour la distance parcourue totale
        """
        d_gauche,d_droite=self.robot.get_distance_roue(self.temps_total)
        d=(d_gauche+d_droite)/2
        self._distanceParcourue+=d
        return d
 
    def calculAngleParcouru(self):
        """
        calcul l'angle parcouru par le robot en radians
        :return: angle parcouru par le robot en radians
        """
        angledif=(self.robot.get_distance_roue(self.temps_total)[1] - self.robot.get_distance_roue(self.temps_total)[0]) / self.robot.WHEEL_BASE_WIDTH
        self._angleParcouru+=angledif
        
    def get_distance_obstacle(self):
        """ 
        retourne la distance a l'obstacle le plus proche d'un obstacle
        """
        return self.robot.get_distance_obstacle()
    

    
class ControleurRobotVraieVie(Controleur):
    """ 
    classe qui permet de controler le robot en vrai vie
    """
    def __init__(self, robot):
        Controleur.__init__(self,robot)
        self.angle_parcouru_offset=(0,0)

    def set_Vitesse(self, dpsg, dpsd):
        """
        met a jour la vitesse des roues du robot    
        :param dpsg: vitesse de la roue gauche en degres par seconde
        :param dpsd: vitesse de la roue droite en degres par seconde
        """
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT, dpsg)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, dpsd)
 
    def calculDistanceParcourue(self):
        """
        calcul la distance parcourue par les roues du robot depuis le dernier appel de la fonction
        :return: la distance parcourue par le robot en mm et met a jour la distance parcourue totale
        """
        motor_pos=self.robot.get_motor_position()

        #calcul la distance parcorue en mm
        distancerg = motor_pos[0]/360 * self.robot.WHEEL_CIRCUMFERENCE
        distancerd = motor_pos[1]/360 * self.robot.WHEEL_CIRCUMFERENCE
        d=(distancerg + distancerd)/2

        #Remet l'offset a 0 pour le prochain appel
        motor_pos=(self.robot.read_encoders()[0],self.robot.read_encoders()[1])

        #mis a jour de la distance parcourue totale
        self._distanceParcourue+=d

        return d 
    
    
    def calculAngleParcouru(self):
        """
        calcul l'angle parcouru par le robot en radians
        :return: angle parcouru par le robot en radians
        """
        motor_pos=self.robot.get_motor_position()

        #calcul la distance parcorue en mm
        distancerg = motor_pos[0]/360 * self.robot.WHEEL_CIRCUMFERENCE
        distancerd = motor_pos[1]/360 * self.robot.WHEEL_CIRCUMFERENCE

        angle=(distancerg-distancerd)/self.robot.WHEEL_BASE_WIDTH

        motor_pos=(self.robot.read_encoders()[0],self.robot.read_encoders()[1])

        self._angleParcouru+=angle
        
        return angle
    
    def __getattr__(self, name):
        return getattr(self.robot, name)
    
