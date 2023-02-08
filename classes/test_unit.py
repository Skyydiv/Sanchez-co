import unittest

from Objet import Robot
from Objet import Obstacle 
from Environnement import *
from Simulation import Simulation


class TestRobot(unittest.TestCase):
        
    def test_r_is_instanceof_Robot(self):
        r=Robot(4,3,10)
        self.assertIsInstance(r,Robot)
        
    def test_setVitesseRoueGauche(self):
        r=Robot(1,3,10)
        r.setVitesseRoueGauche(6)
        self.assertEqual(r.vitesseRoueGauche,6)
        
    def test_setVitesseRoueGauche(self):
        r=Robot(1,3,10)
        r.setVitesseRoueDroite(2)
        self.assertEqual(r.vitesseRoueDroite,2)

    
    def test_tournerDroite(self):
        r=Robot(1,3,10)
        r.tournerDroite()
        self.assertEqual(r.vitesseRoueDroite,0)
            
    def test_tournerGauche(self):
        r=Robot(1,3,10)
        r.tournerGauche()
        self.assertEqual(r.vitesseRoueGauche,0)
        
    def test_arret(self):
        r=Robot(1,3,10)
        r.arret()
        self.assertEqual(r.vitesseRoueGauche,0)
        self.assertEqual(r.vitesseRoueDroite,0)
    
    def test_changerVitesse(self):
        r=Robot(1,3,10)
        r.changerVitesse(5,6)
        self.assertEqual(r.vitesseRoueGauche,5)
        self.assertEqual(r.vitesseRoueDroite,6)
    
    def test_deplacer(self):
         r=Robot(4,3,20)
         self.assertEqual(r.x,r.rayon+0.1)
         r.deplacer()
         self.assertNotEqual(r.x,r.rayon+0.1)
         self.assertNotEqual(r.y,r.rayon+0.1)
        
class TestObstacle(unittest.TestCase):
    
    def test_obstacle_is_instanceof_Obastacle(self):
        
        obstacle=Obstacle(2,3,5,0,4)
        self.assertIsInstance(obstacle,Obstacle)
                                            


class TestEnvironnement(unittest.TestCase):
    
    def setUp(self):
        robot=Robot(1,3,5)
        self.env=Environnement([200,200],robot,2)
        self.env.addObstacle(140,20,5,0,3)
        obs1=Obstacle(140,20,5,0,3)
        obs2=Obstacle(80,170,5,0,3)
        self.env.addObstacle(80,170,5,0,3)
       
    def test_env_is_instanceof_Environnement(self):
        self.assertIsInstance(self.env,Environnement)
        
    def test_estMur(self):
        
        self.assertTrue(self.env.estMur(200,210,5))
        self.assertFalse(self.env.estMur(100,76,5))
    
    def test_estObstacle(self):
        self.assertTrue(self.env.estObstacle(140,21,3))
        self.assertTrue(self.env.estObstacle(140,20,3))
        self.assertTrue(self.env.estObstacle(80,170,3))
        self.assertFalse(self.env.estObstacle(60,20,5))
        
    def test_calculDistance(self):
        obs1=Obstacle(140,20,5,0,3)
        obs2=Obstacle(80,170,5,0,3)
        self.assertEqual(self.env.calculDistance(obs1,obs2),204)
        

class TestSimulation(unittest.TestCase):
    
    
    def test_simu_instanceof_Simulation(self):
        r=Robot(1,3,5)
        envi=Environnement([200,200],r,2)
        simu=Simulation(50,envi)
    
        self.assertIsInstance(simu,Simulation)
    
    
if __name__ == '__main__':
    unittest.main()
    