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

    def get_distance_parcourue(self,delta_t):
        """
        :param delta_t: un intervalle de temps 
        :return: couple de distance parcourue par les 2 roues du robot
        """
        self.robot.get_distance_roue(delta_t)
    


    def __getattr__(self, name):
        return getattr(self.robot, name)
    
class ControleurRobotVraieVie:
    def __init__(self, robot):
        self.robot=robot

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

    def get_distance_parcourue(self,delta_t):
        """
        :param delta_t: un intervalle de temps 
        :return: couple de distance parcourue par les 2 roues du robot
        """
        rotationrg = (self.robot.MOTOR_LEFT * delta_t)
        distancerg = (math.pi * self.robot.WHEEL_DIAMETER/2 * rotationrg) / 180
        rotationrd = (self.robot.MOTOR_RIGHT * delta_t)
        distancerd = (math.pi * self.robot.WHEEL_DIAMETER/2 * rotationrd) / 180
        return (distancerg, distancerd)
    
    def __getattr__(self, name):
        return getattr(self.robot, name)