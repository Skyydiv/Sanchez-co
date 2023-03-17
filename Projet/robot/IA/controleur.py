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
        self.robot.get_distance_roue


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
    
    def __getattr__(self, name):
        return getattr(self.robot, name)