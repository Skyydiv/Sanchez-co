import math 
import time

class Controleur:
    def __init__(self, robot):
        self.robot=robot
        self.deb=0
        self.fin=0
        self.temps_total=0

    def setVitesseRoues(self, vitesseg, vitessed):
        if self.__class__.__name__=="ControleurRobotVirtuel":
            self.robot.setVitesse(vitesseg, vitessed)
        else:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT, vitesseg)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, vitessed)
    
    def avancerToutDroit(self, v):
        if self.__class__.__name__=="ControleurRobotVirtuel":
            self.robot.setVitesse(v,v)
        else:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT, v)

    def tournerDroite(self,v):
        if self.__class__.__name__=="ControleurRobotVirtuel":
            self.robot.setVitesse(v,-v)
        else:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT, v)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, -v)
    
    def tournerGauche(self,v):
        if  self.__class__.__name__=="ControleurRobotVirtuel":
            self.robot.setVitesse(-v,v)
        else:
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT, -v)
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, v)

    def stop(self):
        self.robot.stop()

    def update(self):
        self.fin=time.time()
        self.temps_total=self.fin-self.deb
        self.deb=self.fin

        self.calculDistanceParcourue()
        self.calculAngleParcouru()

    def reset_time(self):
        self.deb=time.time()
        self.temps_total=0


class ControleurRobotVirtuel(Controleur):
    def __init__(self, robot):
        Controleur.__init__(self,robot)
        self.distanceParcourue=0
        self.AngleParcouru=0 #en radians

    def calculDistanceParcourue(self):
        """
        :param delta_t: un intervalle de temps 
        :return: la distance parcourue par le robot pour delta_t et met a jour la distance parcourue totale
        """
        d_gauche,d_droite=self.robot.get_distance_roue(self.temps_total)
        d=(d_gauche+d_droite)/2
        self.distanceParcourue+=d
        return d

    def setDistanceParcourue(self, dist_g,dist_d):
        """fixe la distance parcourue par les roues du robot
        :param dist_g: distance parcourue par la roue gauche
        :param dist_d: distance parcourue par la roue droite
        """
        self.robot.set_distance_parcourue_roue_gauche(dist_g)
        self.robot.set_distance_parcourue_roue_droite(dist_d)

    def setAngleParcouru(self, a):
        """fixe l'angle parcouru par le robot
        :param a: angle parcourue par le robot en degre
        """
        self.robot.set_angle_parcouru(a)
    
    def calculAngleParcouru(self):
        """
        calcul l'angle parcouru par le robot en radians
        :return: angle parcouru par le robot en radians
        """
        #angleRobot=self.robot.angle

        angledif=(self.robot.get_distance_roue(self.temps_total)[1] - self.robot.get_distance_roue(self.temps_total)[0]) / self.robot.WHEEL_BASE_WIDTH
        self.AngleParcouru+=angledif
    
    def getDistanceParcourue(self):
        """
        :return : la distance parcourue par le robot depuis la derniere remise a 0
        """
        return self.distanceParcourue
    
    def getAngleParcouru(self):
        """
        :return : l'angle parcouru par le robot depuis la derniere remise a 0
        """
        return self.AngleParcouru


    # def __getattr__(self, name):
    #     return getattr(self.robot, name)
    
    def resetDistanceParcourue(self):
        self.distanceParcourue=0

    def resetAngleParcourue(self):
        self.AngleParcouru=0
    
class ControleurRobotVraieVie(Controleur):
    def __init__(self, robot):
        Controleur.__init__(self,robot)
        self.distanceParcourue=0
        self.AngleParcouru=0 #en radians
        self.distance_parcourue_roue_gauche=0
        self.distance_parcourue_roue_droite=0
        self.angle_parcouru_offset=(0,0)

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
        self.distanceParcourue+=d

        return d 
    
    
    def setDistanceParcourue(self, dist_g,dist_d):
        """fixe la distance parcourue par les roues du robot
        :param dist_g: distance parcourue par la roue gauche
        :param dist_d: distance parcourue par la roue droite
        """
        self.distance_parcourue_roue_gauche=dist_g
        self.distance_parcourue_roue_droite=dist_d

    def setAngleParcouru(self, a):
        """fixe l'angle parcouru par le robot
        :param a: distance parcourue par le robot en degre
        """
        self.AngleParcouru=a

    def calculAngleParcouru(self,delta_t):
        """
        calcul l'angle parcouru par le robot en radians
        :return: angle parcouru par le robot en radians
        """
        pos=self.robot.get_motor_position()
        posL=(pos[0]-self.angle_parcouru_offset[0])/360 * self.robot.WHEEL_DIAMETER * math.pi
        posR=(pos[1]-self.angle_parcouru_offset[1])/360 * self.robot.WHEEL_DIAMETER * math.pi

        angle= (posR-posL)/self.robot.WHEEL_BASE_WIDTH

        self.angle_parcouru_offset=(pos[0],pos[1])
        return angle
    
    def getDistanceParcourue(self):
        """
        :return : la distance parcourue par le robot depuis la derniere remise a 0
        """
        return self.distanceParcourue
    
    def getAngleParcouru(self):
        """
        :return : l'angle parcouru par le robot depuis la derniere remise a 0
        """
        return self.AngleParcouru

    def __getattr__(self, name):
        return getattr(self.robot, name)
    
    
    def resetDistanceParcourue(self):
        self.distanceParcourue=0
