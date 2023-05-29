import unittest
import math
from robot.simu.virtuel import Robot, Environnement, Obstacle
from robot.simu.simulation import Simulation

class TestRobot(unittest.TestCase):
        
    def test_r_is_instanceof_Robot(self):
        """
        Vérifie si l'objet créé est une instance de la classe Robot.
        """
        r = Robot(4)
        self.assertIsInstance(r, Robot)
        
    def test_setVitesse(self):
        """
        Vérifie si la méthode setVitesse du robot fonctionne correctement
        et a bien mis le robot à la vitesse souhaitée.
        """
        r = Robot(4)
        r.setVitesse(6, 5)
        self.assertEqual(r.vitesseRoueGauche, 5)
        self.assertEqual(r.vitesseRoueDroite, 6)
        
class TestObstacle(unittest.TestCase):
    
    def test_obstacle_is_instanceof_Obastacle(self):
        """
        Vérifie si l'objet créé est une instance de la classe Obstacle.
        """
        obstacle = Obstacle(2, 3, 5, 0, 4)
        self.assertIsInstance(obstacle, Obstacle)
                                            

class TestEnvironnement(unittest.TestCase):
    
    def setUp(self):
        """
        Configuration initiale pour les tests de la classe Environnement.
        """
        robot = Robot(5)
        self.env = Environnement([200, 200], robot, 2)
        self.env.addObstacle(140, 20, 5, 0, 3)
        self.env.addObstacle(80, 170, 5, 0, 3)
        self.env.addObstacle(10, 10, 5, 0, 3)
       
    def test_env_is_instanceof_Environnement(self):
        """
        Vérifie si l'objet créé est une instance de la classe Environnement.
        """
        self.assertIsInstance(self.env, Environnement)
        
    def test_estMur(self):
        """
        Vérifie si la méthode estMur de l'environnement renvoie les résultats attendus.
        """
        self.assertTrue(self.env.estMur(2, -1, 5))
        self.assertFalse(self.env.estMur(100, 76, 5))
    
    def test_estObstacle(self):
        """
        Vérifie si la méthode estObstacle de l'environnement renvoie les résultats attendus
        et donc que l'obstacle a bien été créé.
        """
        self.assertFalse(self.env.estObstacle(80,90,5))
        self.assertTrue(self.env.estObstacle(140,20,5))
        self.assertFalse(self.env.estObstacle(12,12,5))
        self.assertFalse(self.env.estObstacle(40,40,1))
        
    
class TestSimulation(unittest.TestCase):
    
    
    def test_simu_instanceof_Simulation(self):
        """
        Vérifie si l'objet créé est une instance de la classe Simulation.
        """
        r = Robot(5)
        envi = Environnement([200, 200], r, 2)
        simu = Simulation(50)
    
        self.assertIsInstance(simu, Simulation)


        
if __name__ == '__main__':
    unittest.main()
