import unittest

from montecarlo import Die, Game, Analyzer

class DieTestSuite(unittest.TestCase):
    #create a die with specified faces and test if it exists
    def test_1_create_die(self):
        faces_array = np.array([1,2,3,4,5,6])
        die = Die(faces_array, weight = 1.0)
    
    #error message in case test fails
    message = "Die creation failed"
    
    #assertTrue
    self.assertTrue('Die created! Yay!', message)
    
    self.die = die
    
    print(die)
 
        
    def test_2_update_weight(self):
        #update the weights of the die for a given face
        self.die.update_weight(1, 7.0)
        
        #error message in case test fails
        message = 'Die weight did NOT update'
        #assertTrue
        self.asserTrue('Die weight updated! Yay!', message)
        
    def test_3_roll(self):
        #roll the die 3 times
        result = self.die.roll(3)
        print(result)
        
        #error message in case test fails
        message = 'Die did NOT roll'
        
        #assertTrue
        self.asserTrue('Die rolled! Yay!', message)
        
    def test_4_die_curr_state(self):
        #show the current state of the die
        self.die.die_current_state()
        
if __name__ == '__main__':
    unittest.main(verbosity=3)