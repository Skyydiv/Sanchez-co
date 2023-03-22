import math 

class ControleurRobotVirtuel:
    def __init__(self, robot):
        self.robot=robot
        self.distanceParcourue=0
        self.AngleParcouru=0 #en radians


    def setVitesseRoues(self, vitesseg, vitessed):
        self.robot.setVitesse(vitesseg,vitessed)

    def avancerToutDroit(self, v):
        self.calculDistanceParcourue
        self.robot.setVitesse(v,v)

    def tournerDroite(self,v):
        self.robot.setVitesse(v,-v)
    
    def tournerGauche(self,v):
        self.robot.setVitesse(-v,v)

    def stop(self):
        self.robot.setVitesse(0,0)

    def calculDistanceParcourue(self,delta_t):
        """
        :param delta_t: un intervalle de temps 
        :return: la distance parcourue par le robot pour delta_t et met a jour la distance parcourue totale
        """
        d_gauche,d_droite=self.robot.get_distance_roue(delta_t)
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

        delta_t=100
        angledif=(self.robot.get_distance_roue(delta_t)[1] - self.robot.get_distance_roue(delta_t)[0]) / self.robot.WHEEL_BASE_WIDTH
        self.AngleParcouru+=angledif
    
    def getDistanceParcourue(self):
        """
        :return : la distance parcourue par le robot depuis la derniere remise a 0
        """
        return self.distanceParcourue


    # def __getattr__(self, name):
    #     return getattr(self.robot, name)
    
    def resetDistanceParcourue(self):
        self.distanceParcourue=0

    def resetAngleParcourue(self):
        self.AngleParcouru=0
    
class ControleurRobotVraieVie:
    def __init__(self, robot):
        self.robot=robot
        self.distanceParcourue=0
        self.distance_parcourue_roue_gauche=0
        self.distance_parcourue_roue_droite=0
        self.angle_parcouru_offset=(0,0)

    def setVitesseRoues(self, dpsg, dpsd):
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT, dpsg)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, dpsd)

    def avancerToutDroit(self, dps,delta_t):
        self.calculDistanceParcourue(delta_t)
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, dps)

    def tournerDroite(self,dps):
        self.calculAngleParcouru()
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT, dps)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, -dps)
    
    def tournerGauche(self,dps):
        self.calculAngleParcouru()
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT, -dps)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, dps)

    def stop(self):
        self.robot.stop()

    def calculDistanceParcourue(self,delta_t):
        """
        calcul la distance parcourue par les roues du robot
        :param delta_t: un intervalle de temps 
        :return: la distance parcourue par le robot pour delta_t et met a jour la distance parcourue totale
        """
        rotationrg = (self.robot.MOTOR_LEFT * delta_t)
        distancerg = (math.pi * self.robot.WHEEL_DIAMETER/2 * rotationrg) / 180
        rotationrd = (self.robot.MOTOR_RIGHT * delta_t)
        distancerd = (math.pi * self.robot.WHEEL_DIAMETER/2 * rotationrd) / 180
        d=(distancerg + distancerd)/2
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
        self.angle_parcouru=a

    def calculAngleParcouru(self):
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

    def __getattr__(self, name):
        return getattr(self.robot, name)
    
    
    def resetDistanceParcourue(self):
        self.distanceParcourue=0
