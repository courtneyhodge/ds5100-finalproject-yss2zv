import unittest
import pandas as pd
import numpy as np

from montecarlo import Die, Game, Analyzer

class DieTestSuite(unittest.TestCase):
    #create a die with specified faces and test if it exists
        
    def test_01_create_die(self):
        #make an instance of a six sided die
        faces_array = np.array([1,2,3,4,5,6])
        
        #------start-test-------#
        #innitialize this die, passing a weight of 1.0
        die = Die(faces_array, weight = 1.0)
        flag = True
        
        if(not isinstance(die, Die)): #see if die is of type Die
            flag = False
        #------end-test---------#
        
        #------start-assertion------#
        #error message in case test fails
        message = "Die creation failed"

        #assertTrue
        self.assertTrue(flag, message)
        #------end-assertion------#
        
    def test_02_update_weight(self):
        #innitialize die
        faces_array = np.array([1,2,3,4,5,6])
        die = Die(faces_array, weight = 1.0)
        
        #------start-test-------#
        #update the weights of the die for face "1"
        die.update_weight(1, 7.0)
        
        updated_weight = die._private_data_frame.loc[die._private_data_frame['faces'] == 1, 'weights'].values[0]
        
        flag = (updated_weight == 7.0)
        #------end-test---------#
        
        #------start-assertion------#        
        #error message in case test fails
        message = 'Die weight did NOT update'
        #assertTrue
        self.assertTrue(flag, message)
        #------end-assertion------#
        
    def test_03_roll(self):
        #innitialize die
        faces_array = np.array([1,2,3,4,5,6])
        self.die = Die(faces_array, weight = 1.0)
        
        #------start-test-------#
        #roll the die 3 times
        print(self.die.roll(3))
        flag = True
        
        if(len(self.die.roll(3)) != 3): #see if the die rolled 3 times
            flag = False
        #------end-test---------#
        
        #------start-assertion------#
        #error message in case test fails
        message = 'Die did NOT roll'
        
        #assertTrue
        self.assertTrue(flag, message)
        #------end-assertion------#
        
    def test_04_die_curr_state(self):
        #innitialize die
        faces_array = np.array([1,2,3,4,5,6])
        die = Die(faces_array, weight = 1.0)
        
        #------start-test-------#
        print(die.die_current_state())
        flag = True
        
        if(not isinstance(die.die_current_state(), pd.DataFrame)): #check if the current die state df exists (shows results)
            flag = False
        #------end-test---------#
        
        #------start-assertion------#
        #error message in case test fails
        message = 'Die did NOT roll'
        
        #assertTrue
        self.assertTrue(flag, message)
        #------end-assertion------#
           
    def test_05_create_game(self):
        #innitialize a die
        faces_array = np.array([1,2,3,4,5,6])
        die = Die(faces_array, weight = 1.0)
        
        #make many of die
        dice = [die for _ in range(7)]
        
        #------start-test-------#
        #create an instance of a game
        game = Game(dice)
        flag = True
        
        if(not isinstance(game, Game)):
            flag = False
        #------end-test---------#
        
        #------start-assertion------#
        #error message in case test fails
        message = 'Game was NOT created'
        
        #assertTrue
        self.assertTrue(flag, message)
        #------end-assertion------#
        
    def test_06_play(self):
        #innitialize a die
        faces_array = np.array([1,2,3,4,5,6])
        die = Die(faces_array, weight = 1.0)
        
        #make many of die
        dice = [die for _ in range(7)]
        
        #create an instance of a game
        game = Game(dice)
        
        #------start-test-------#
        #play the game
        game.play(100)
        flag = True
        
        if(not isinstance(game._private_data_frame_2, pd.DataFrame)):
            flag = False
        #------end-test---------#
        
        #------start-assertion------#
        #error message in case test fails
        message = 'Game was NOT played. PLAY THE DAMN GAME! please!'
        
        #assertTrue
        self.assertTrue(flag, message)
        #------end-assertion------#
    
    def test_07_show_results(self):
        #innitialize a die
        faces_array = np.array([1,2,3,4,5,6])
        die = Die(faces_array, weight = 1.0)
        
        #make many of die
        dice = [die for _ in range(7)]
        
        #create an instance of a game
        game = Game(dice)
        
        #play the game
        game.play(100)
        
        #------start-test-------#
        #show results
        print(game.show_results())
        flag = True
        
        if(not isinstance(game.show_results(), pd.DataFrame)):
            flag = False
        
        #------end-test---------#
        
        #------start-assertion------#
        #error message in case test fails
        message = 'Game results were not shown'
        
        #assertTrue
        self.assertTrue(flag, message)
        #------end-assertion------#
        
    def test_08_create_game_to_analyze(self):
        #innitialize a die
        faces_array = np.array([1,2,3,4,5,6])
        die = Die(faces_array, weight = 1.0)
        
        #make many of die
        dice = [die for _ in range(7)]
        
        #create an instance of a game
        game = Game(dice)
        
        #------start-test-------#
        #create an analyzer instance
        analyzer = Analyzer(game)
        flag = True
        
        if(not isinstance(analyzer, Analyzer)):
            flag = False
        #------end-test---------#
        
        #------start-assertion------#
        #error message in case test fails
        message = 'Analyzer instance was NOT created'
        
        #assertTrue
        self.assertTrue(flag, message)
        #------end-assertion------#
        
    def test_09_jackpot(self):
        #innitialize a die
        faces_array = np.array([1,2,3,4,5,6])
        die = Die(faces_array, weight = 9.0) #adding a heavy weight for jackpots
        
        #make many of die
        dice = [die for _ in range(7)]
        
        #create an instance of a game
        game = Game(dice)
        
        #play the game
        game.play(10)
        
        #create an analyzer instance
        analyzer = Analyzer(game)
        
        #------start-test-------#
        print(analyzer.jackpot())
        flag = True
        
        if(not isinstance(analyzer.jackpot(), int)):
            flag = False
        #------end-test---------#
        
        #------start-assertion------#
        #error message in case test fails
        message = 'Jackpot is not a returned integer'
        
        #assertTrue
        self.assertTrue(flag, message)
        #------end-assertion------#
        
    def test_10_face_values(self):
        #innitialize a die
        faces_array = np.array([1,2,3,4,5,6])
        die = Die(faces_array, weight = 9.0) #adding a heavy weight for jackpots
        
        #make many of die
        dice = [die for _ in range(7)]
        
        #create an instance of a game
        game = Game(dice)
        
        #play the game
        game.play(10)
        
        #create an analyzer instance
        analyzer = Analyzer(game)
        
        #------start-test-------#
        print(analyzer.face_values())
        flag = True
        
        if(not isinstance(analyzer.face_values(), pd.DataFrame)):
            flag = False
        #------end-test---------#
        
        #------start-assertion------#
        #error message in case test fails
        message = 'Face values was NOT returned'
        
        #assertTrue
        self.assertTrue(flag, message)
        #------end-assertion------#
        
    def test_11_combination(self):
        #innitialize a die
        faces_array = np.array([1,2,3,4,5,6])
        die = Die(faces_array, weight = 9.0) #adding a heavy weight for jackpots
        
        #make many of die
        dice = [die for _ in range(7)]
        
        #create an instance of a game
        game = Game(dice)
        
        #play the game
        game.play(10)
        
        #create an analyzer instance
        analyzer = Analyzer(game)
        
        #------start-test-------#
        print(analyzer.combination_count())
        flag = True
        
        if(not isinstance(analyzer.combination_count(), pd.DataFrame)):
            flag = False
            
        #------end-test---------#
        
        #------start-assertion------#
        #error message in case test fails
        message = 'Combination df was NOT retunred'
        
        #assertTrue
        self.assertTrue(flag, message)
        #------end-assertion------#    
        
    def test_12_permutation(self):
        #innitialize a die
        faces_array = np.array([1,2,3,4,5,6])
        die = Die(faces_array, weight = 9.0) #adding a heavy weight for jackpots
        
        #make many of die
        dice = [die for _ in range(7)]
        
        #create an instance of a game
        game = Game(dice)
        
        #play the game
        game.play(10)
        
        #create an analyzer instance
        analyzer = Analyzer(game)
        
        #------start-test-------#
        print(analyzer.permutation_count())
        flag = True
        
        if(not isinstance(analyzer.permutation_count(), pd.DataFrame)):
            flag = False        
        #------end-test---------#
        
        #------start-assertion------#
        #error message in case test fails
        message = 'Permutation df was NOT retunred'
        
        #assertTrue
        self.assertTrue(flag, message)
        #------end-assertion------# 
        
if __name__ == '__main__':
    unittest.main(verbosity=3)