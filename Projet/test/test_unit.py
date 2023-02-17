import unittest
from simu import *

class TestRobot(unittest.TestCase):
        
    def test_r_is_instanceof_Robot(self):
        c=Capteur(6)
        r=Robot(4,c)
        self.assertIsInstance(r,Robot)
        
    def test_setVitesse(self):
        c=Capteur(6)
        r=Robot(4,c)
        r.setVitesse(6,5)
        self.assertEqual(r.vitesseRoueGauche,5)
        self.assertEqual(r.vitesseRoueDroite,6)
        
    def test_set_motor_dps(self):
        c=Capteur(6)
        r=Robot(4,c)
        r.set_motor_dps(None, 10)
        self.assertEqual(r.MOTOR_RIGHT,10)
        self.assertEqual(r.MOTOR_LEFT,10)
        
class TestObstacle(unittest.TestCase):
    
    def test_obstacle_is_instanceof_Obastacle(self):
        
        obstacle=Obstacle(2,3,5,0,4)
        self.assertIsInstance(obstacle,Obstacle)
                                            


class TestEnvironnement(unittest.TestCase):
    
    def setUp(self):
        c=Capteur(6)
        robot=Robot(5,c)
        self.env=Environnement([200,200],robot,2)
        self.env.addObstacle(140,20,5,0,3)
        obs1=Obstacle(140,20,5,0,3)
        obs2=Obstacle(80,170,5,0,3)
        self.env.addObstacle(80,170,5,0,3)
        self.env.addObstacle(10,10,5,0,3)
       
    def test_env_is_instanceof_Environnement(self):
        self.assertIsInstance(self.env,Environnement)
        
    def test_estMur(self):
        
        self.assertTrue(self.env.estMur(2,-1,5))
        self.assertFalse(self.env.estMur(100,76,5))
    
    def test_estObstacle(self):
        self.assertTrue(self.env.estObstacle(140,21,5))
        self.assertTrue(self.env.estObstacle(140,20,5))
        self.assertTrue(self.env.estObstacle(80,170,5))
        self.assertTrue(self.env.estObstacle(80,171,5))
        self.assertTrue(self.env.estObstacle(10,10,5))
        self.assertTrue(self.env.estObstacle(12,12,5))
        self.assertFalse(self.env.estObstacle(40,40,1))
        
    def test_calculDistance(self):
        obs1=Obstacle(140,20,5,0,3)
        obs2=Obstacle(80,170,5,0,3)
        self.assertEqual(self.env.calculDistance(obs1,obs2),161.53637361288014)
        

class TestSimulation(unittest.TestCase):
    
    
    def test_simu_instanceof_Simulation(self):
        cap=Capteur(6)
        r=Robot(5,cap)
        envi=Environnement([200,200],r,2)
        simu=Simulation(envi,50)
    
        self.assertIsInstance(simu,Simulation)
    
    
if __name__ == '__main__':
    unittest.main()
