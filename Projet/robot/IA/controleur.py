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
        self.set_Vitesse(vitesseg, vitessed)
    
    def avancerToutDroit(self, v):
        self.set_Vitesse(v,v)

    def tournerDroite(self,v):
        self.set_Vitesse(v,-v)
    
    def tournerGauche(self,v):
        self.set_Vitesse(-v,v)

    def stop(self):
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
        self._distanceParcourue=0

    def resetAngleParcourue(self):
        self._angleParcouru=0


class ControleurRobotVirtuel(Controleur):
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
    
    
class ControleurRobotVraieVie(Controleur):
    def __init__(self, robot):
        Controleur.__init__(self,robot)
        self.angle_parcouru_offset=(0,0)

    def set_Vitesse(self, dpsg, dpsd):
        self.robot.set_motor_dps(self.MOTOR_LEFT, dpsg)
        self.robot.set_motor_dps(self.MOTOR_RIGHT, dpsd)
 
    def calculDistanceParcourue(self):
        """
        calcul la distance parcourue par les roues du robot depuis le dernier appel de la fonction
        :return: la distance parcourue par le robot en mm et met a jour la distance parcourue totale
        """
        motor_pos=self.get_motor_position()

        #calcul la distance parcorue en mm
        distancerg = motor_pos[0]/360 * self.WHEEL_CIRCUMFERENCE
        distancerd = motor_pos[1]/360 * self.WHEEL_CIRCUMFERENCE
        d=(distancerg + distancerd)/2

        #Remet l'offset a 0 pour le prochain appel
        self.offset_motor_encoder(self.MOTOR_LEFT, self.read_encoders()[0])
        self.offset_motor_encoder(self.MOTOR_RIGHT, self.read_encoders()[1])

        #mis a jour de la distance parcourue totale
        self._distanceParcourue+=d

        return d 
    
    
    def calculAngleParcouru(self):
        """
        calcul l'angle parcouru par le robot en radians
        :return: angle parcouru par le robot en radians
        """
        #recuperation de la position des moteurs
        pos=self.robot.get_motor_position()
        #calcul de la position du moteur gauche
        posL=(pos[0]-self.angle_parcouru_offset[0])/360 * self.robot.WHEEL_DIAMETER * math.pi
        #calcul de la position du moteur droit
        posR=(pos[1]-self.angle_parcouru_offset[1])/360 * self.robot.WHEEL_DIAMETER * math.pi

        #calcul de l'angle parcouru
        angle=(posR-posL)/self.robot.WHEEL_BASE_WIDTH

        #mise a jour de l'offset
        self.angle_parcouru_offset=(pos[0],pos[1])
        #mise a jour de l'angle parcouru
        self._angleParcouru+=angle
        
        return angle
    
    def __getattr__(self, name):
        return getattr(self.robot, name)
    
