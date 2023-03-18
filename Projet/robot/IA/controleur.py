import math 

class ControleurRobotVirtuel:
    def __init__(self, robot):
        self.robot=robot

    def avancerToutDroit(self, v):
        self.robot.setVitesse(v,v)

    def tournerDroite(self,v):
        self.robot.setVitesse(v,0)
    
    def tournerGauche(self,v):
        self.robot.setVitesse(0,v)

    def stop(self):
        self.robot.setVitesse(0,0)

    def calculDistanceParcourue(self,delta_t):
        """
        :param delta_t: un intervalle de temps 
        :return: couple de distance parcourue par les 2 roues du robot
        """
        return self.robot.get_distance_roue(delta_t)

    def setDistanceParcourue(self, dist_g,dist_d):
        """fixe la distance parcourue par les roues du robot
        :param dist_g: distance parcourue par la roue gauche
        :param dist_d: distance parcourue par la roue droite
        """
        self.robot.set_distance_parcourue_roue_gauche(dist_g)
        self.robot.set_distance_parcourue_roue_droite(dist_d)

    def setAngleParcouru(self, a):
        """fixe l'angle parcouru par le robot
        :param a: distance parcourue par le robot en degre
        """
        self.robot.set_angle_parcouru(a)
    
    def calculAngleParcouru(self, delta_t):
        angleRobot=self.robot.angle
        angleParcouru=(self.robot.get_distance_roue(delta_t)[1] - self.robot.get_distance_roue(delta_t)[0]) / self.robot.WHEEL_BASE_WIDTH
        self.robot.angle=angleParcouru+angleRobot
        return angleParcouru
    


    def __getattr__(self, name):
        return getattr(self.robot, name)
    
class ControleurRobotVraieVie:
    def __init__(self, robot):
        self.robot=robot
        self.distance_parcourue_roue_gauche=0
        self.distance_parcourue_roue_droite=0
        self.angle_parcouru=0 #en degre

    def avancerToutDroit(self, dps):
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT, dps)

    def tournerDroite(self,dps):
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT, dps)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, 0)
    
    def tournerGauche(self,dps):
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT, 0)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT, dps)

    def stop(self):
        self.robot.stop()

    def calculDistanceParcourue(self,delta_t):
        """
        :param delta_t: un intervalle de temps 
        :return: couple de distance parcourue par les 2 roues du robot
        """
        rotationrg = (self.robot.MOTOR_LEFT * delta_t)
        distancerg = (math.pi * self.robot.WHEEL_DIAMETER/2 * rotationrg) / 180
        rotationrd = (self.robot.MOTOR_RIGHT * delta_t)
        distancerd = (math.pi * self.robot.WHEEL_DIAMETER/2 * rotationrd) / 180
        return (distancerg, distancerd)
    
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
        angleRobot=self.robot.angle
        angleParcouru=(self.distance_parcourue_roue_droite - self.distance_parcourue_roue_gauche) / self.robot.WHEEL_BASE_WIDTH
        self.robot.angle=angleParcouru+angleRobot
        return angleParcouru
        

    def __getattr__(self, name):
        return getattr(self.robot, name)