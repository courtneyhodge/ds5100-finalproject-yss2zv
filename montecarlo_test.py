import unittest
import pandas as pd
import numpy as np

from montecarlo import Die, Game, Analyzer

class DieTestSuite(unittest.TestCase):
    #create a die with specified faces and test if it exists
        
    def test_1_create_die(self):
        #make an instance of a six sided die
        faces_array = np.array([1,2,3,4,5,6])
        
        #innitialize this die, passing a weight of 1.0
        self.die = Die(faces_array, weight = 1.0)
        
        #------start-assertion------#
    
        #error message in case test fails
        message = "Die creation failed"

        #assertTrue
        self.assertTrue('Die created! Yay!', message)
        #------end-assertion------#
        
    def test_2_update_weight(self):
        #innitialize die
        faces_array = np.array([1,2,3,4,5,6])
        self.die = Die(faces_array, weight = 1.0)
        
        #update the weights of the die for a particular face
        self.die.update_weight(1, 7.0)
        
        #------start-assertion------#        
        #error message in case test fails
        message = 'Die weight did NOT update'
        #assertTrue
        self.assertTrue('Die weight updated! Yay!', message)
        #------end-assertion------#
        
    def test_3_roll(self):
        #innitialize die
        faces_array = np.array([1,2,3,4,5,6])
        self.die = Die(faces_array, weight = 1.0)
        
        #roll the die 3 times
        result = self.die.roll(3)
        print(result)
        
        #------start-assertion------#
        #error message in case test fails
        message = 'Die did NOT roll'
        
        #assertTrue
        self.assertTrue('Die rolled! Yay!', message)
        #------end-assertion------#
        
    def test_4_die_curr_state(self):
        #innitialize die
        faces_array = np.array([1,2,3,4,5,6])
        self.die = Die(faces_array, weight = 1.0)
        
        #show the current state of the die
        #self.die.die_current_state()
        
        
class GameTestSuite(unittest.TestCase):
    
    def test_5_create_game(self):
        #innitialize a die
        faces_array = np.array([1,2,3,4,5,6])
        die = Die(faces_array, weight = 1.0)
        
        #make a couple of dice
        dice = [die for _ in range(7)]
        
        #create an instance of a game
        game = Game(dice)
        
        
        pass
        
        
if __name__ == '__main__':
    unittest.main(verbosity=3)