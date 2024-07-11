import numpy as np
import pandas as pd

import numpy as np
import pandas as pd

class Die():
    '''
    General Purpose: A class that creates a die object for the project with distinct faces and
    adjustable weights.
    '''

    def __init__(self, faces, weight = 1.0):                        #W defualts to 1.0
        '''
        Initializes the die with a list of faces.

        Parameters:
        -----------
        faces : np.ndarray
            A NumPy array of unique faces for the die.
        weight : float, optional
            The initial weight for each face (default is 1.0).

        Raises:
        -------
        TypeError:
            If faces is not a NumPy array or contains invalid types.
        ValueError:
            If faces do not contain unique values.
        '''

        if(not isinstance(faces, np.ndarray)):                      #Throws TypeError if faces is not a NumPy array
            raise TypeError("Faces must be a NumPy array")

        if faces.dtype == object:                                   #checks if string contains objects and type casts as int
            for element in faces:
                try:
                    int(element)
                except:
                    raise TypeError("wrong type: all faces must be strings or numbers") #if this doesn't work, raise TypeError

        elif np.issubdtype(faces.dtype, np.integer):                #check if sub dtypes of faces are ints
            pass 

        elif np.issubdtype(faces.dtype, np.floating):               #check if sub dtypes of faces are floats
            pass

        elif np.issubdtype(faces.dtype, np.str_):                   #check if sub dtypes of faces are str
            pass

        else:
            raise TypeError("wrong type: all faces must be strings or numbers") #if none of the above, raise TypeError

        if(len(np.unique(faces)) != len(faces)):                    #check if each value is unique in faces, if not, raise ValueError
            raise ValueError("duplicate values: faces must be distinct")
        else:
            pass

        self.faces = faces

        if((type(weight) == float) or (type(weight) == int) or (type(weight) == str)): #check if the weight is castable to float
            if(type(weight) == str):
                weight = float(weight)
            elif(type(weight) == int):
                weight = float(weight)
        self.weight = np.ones_like(faces, dtype = float) * weight   #initialize weights to 1.0 for each face AND allows for the
                                                                    #weights to update if a float other than 1.0 is provided

        self._private_data_frame = pd.DataFrame({"faces": faces, "weights": weight}) #save faces and weights in a private df


    def update_weight(self, face_value_to_change, new_weight):      #function to update a face weight, ie make it an unfair die
        '''
        Takes two arguments: the face value to be changed and the new weight.

        Parameters:
        -----------
        face_value_to_change : int, float, or str
            The face value whose weight is to be changed.
        new_weight : int, float, or str
            The new weight for the specified face.

        Raises:
        -------
        IndexError:
            If the face value is not found in the die.
        TypeError:
            If the new weight is not a valid type (int, float, or str).
        '''

        if(face_value_to_change in self.faces):                     #if the face value to change is found in the die...
            if((type(new_weight) == float) or (type(new_weight) == int) or (type(new_weight) == str)): #check if the weight is castable to float
                if(type(new_weight) == str):
                    new_weight = float(new_weight)
                elif(type(new_weight) == int):
                    new_weight = float(new_weight)
                self.weight[self.faces == face_value_to_change] = new_weight                            #update the weight of a single face
                self._private_data_frame.loc[self._private_data_frame["faces"] == face_value_to_change, #update the weight of a single face THIS IS SO ESSENTIAL!
                                             "weights"] = new_weight
            else:
                raise TypeError("type error: new weight must be a float, int, or string")               #if the weight is not castable, raise TypeError
        else:
            raise IndexError("index error: face value not in die")  #if the face value to change is NOT found in the die, throw an IndexError


    def roll(self, num_of_rolls = 1):                               #function to roll the die one or more times
        '''
        Takes a parameter of how many times the die is to be rolled;
        defaults to 1. This is essentially a random sample with replacement,
        from the private die data frame, that applies the weights. Returns
        a Python list of outcomes. Does not store internally these results.

        Parameters:
        -----------
        num_of_rolls : int, optional
            The number of times to roll the die (default is 1).

        Returns:
        --------
        list
            A list of outcomes from the rolls.
        '''

        return self._private_data_frame.sample(n = num_of_rolls, replace = True,             #convert the df to a list as specified
                                               weights = self.weight).faces.tolist()


    def die_current_state(self):
        """
        Returns a copy of the private die data frame to the user.

        Returns:
        --------
        pd.DataFrame
            A copy of the DataFrame containing faces and their current weights.
        """

        return self._private_data_frame.copy()    
    
    
class Game():
    '''
    General Purpose: A class representing a game played with a list of dice.
    '''
    def __init__(self, dice):
        '''
        Initializes the game with a list of dice. Checks if all objects in
        dice_list are instances of Die. If not, raises a ValueError.

        Parameters:
        -----------
        dice_list : List[Die]
            A list of already instantiated similar dice.

        Raises:
        -------
        ValueError:
            If any object in dice_list is not an instance of Die.
        '''
        if all(isinstance(die, Die) for die in dice):                 #check if all objects in dice_list are instances of Die
            self.dice = dice                                     #if so, set self.dice_list to dice_list
        else:
            raise ValueError("value error: all objects in dice_list must be instances of Die")
            
        
    def play(self, num_rolls):
        '''
        Takes an integer parameter to specify how many times the dice should
        be rolled. Saves the result of the play to a private data frame.
        The data frame should be in wide format, i.e. have the roll number
        as a named index, columns for each die number (using its list index
        as the column name), and the face rolled in that instance in each
        cell.

        Parameters:
        -----------
        num_rolls : int
            The number of times the dice should be rolled.
        '''
        result_dict = {f'Die_{i}': [] for i in range(len(self.dice))} #create a dictionary to store the results in

        for i in range(num_rolls):                                         #roll the dice num_rolls times
            for j, die in enumerate(self.dice):                       #roll each die in the list
                result_dict[f'Die_{j}'].extend(die.roll(1))                #append the result of the roll to the dictionary

        self._private_data_frame_2 = pd.DataFrame(result_dict)             #save the results in a private data frame
        self._private_data_frame_2.index.name = "Roll Number"              #set the index name to "Roll Number"

    def show_results(self, wide_or_narrow = "wide"):
        '''
        This method just returns a copy of the private play data frame to
        the user. Takes a parameter to return the data frame in narrow or wide form
        which defaults to wide form. The narrow form will have a MultiIndex,
        comprising the roll number and the die number (in that order), and a
        single column with the outcomes (i.e. the face rolled).

        Parameters:
        -----------
        wide_or_narrow : str, optional
            Specifies whether to return the data frame in 'wide' or 'narrow' format (default is 'wide').

        Returns:
        --------
        pd.DataFrame
            A copy of the private data frame either in wide or narrow format.

        Raises:
        -------
        ValueError:
            If the user passes an invalid option for wide_or_narrow.
        '''
        if(wide_or_narrow == "wide"):
            return self._private_data_frame_2.copy()

        elif(wide_or_narrow == "narrow"):
            narrow_df = self._private_data_frame_2.stack().reset_index()   #stack the data frame and reset the index
            narrow_df.columns = ["Roll Number", "Die Number", "Outcomes"]  #set the column names


            return narrow_df.set_index(['Roll Number', 'Die Number'])      #set the index to the roll number and die number

        else:
            raise ValueError("value error: use either 'wide' or 'narrow'")
        
    
    
class Analyzer():
    """
    General Purpose: A class for analyzing outcomes from a game.
    """

    def __init__(self, game):
        """
        Initializes the analyzer with a game object. Throws a ValueError if the
        passed value is not a Game object.

        Parameters:
        -----------
        game : Game
            An instance of the Game class representing the game to analyze.

        Raises:
        -------
        ValueError:
            If game is not an instance of the Game class.
        """
        if not isinstance(game, Game):
            raise ValueError("value error: game must be an instance of Game")
        self.game = game

    def jackpot(self):
        '''
        A jackpot is a result in which all faces are the same, e.g. all ones
        for a six-sided die. Computes how many times the game resulted in a jackpot.

        Returns:
        --------
        int
            The number of jackpots.
        '''
        df = self.game.show_results()     #grab the current game's df

        jackpot_count = 0
        for _, row in df.iterrows():  #iterate through each row in the df
            if row.nunique() == 1:              #check if nunique is 1 (meaning each die rolls the same number on a given roll)
                jackpot_count += 1

        return jackpot_count

    def face_values(self):
        '''
        Computes how many times a given face is rolled in each event.

        Returns:
        --------
        pd.DataFrame
            DataFrame showing the count of each face rolled in each event.
            Index represents the roll number, columns represent face values.
        '''
        df = self.game.show_results("wide")

        all_faces = sorted(set(face for die in self.game.dice for face in die.faces)) #get all faces from all dice

        face_df = pd.DataFrame(0, index = df.index, columns = all_faces) #create a dataframe to store the results

        for roll_number, row in df.iterrows():                           #iterate through each row in the df
            face_counts = row.value_counts()                             #get the count of each face in the row
            for face in all_faces:                                       #iterate through all faces
                face_df.at[roll_number, face] = face_counts.get(face, 0) #store the count of the face in the dataframe

        return face_df

    def combination_count(self):
        '''
        Computes the distinct combinations of faces rolled, along with their
        counts. Combinations are order-independent and may contain repetitions.

        Returns:
        --------
        pd.DataFrame
            DataFrame with MultiIndex of distinct combinations and a column
            for the associated counts.
        '''
        df = self.game.show_results("wide")

        sorted_rows = df.apply(lambda x: tuple(sorted(x)), axis=1) #ensure order independency, aligning with method requirements


        #sorted_rows_to_list = sorted_rows.tolist()                 #convert the series to a list

        combo_counts = sorted_rows.value_counts().sort_index()     #count the number of times each combination occurs

        combo_df = combo_counts.reset_index(name='Count')          #reset the index to a column

        combo_df.columns = ['Combination', 'Count']                #rename the columns

        combo_df.set_index('Combination', inplace=True)            #set the index to the combination

        return combo_df

    def permutation_count(self):
        '''
        Computes the distinct permutations of faces rolled, along with their
        counts. Permutations are order-dependent and may contain repetitions.

        Returns:
        --------
        pd.DataFrame
            DataFrame with MultiIndex of distinct permutations and a column
            for the associated counts.
        '''
        df = self.game.show_results("wide")

        perm_rows = df.apply(tuple, axis=1)                 #ensure order independency, aligning with method requirements

        perm_counts = perm_rows.value_counts().sort_index() #count the number of times each permutation occurs

        perm_df = perm_counts.reset_index(name='Count')     #reset the index to a column

        perm_df.columns = ['Permutation', 'Count']          #rename the columns

        perm_df.set_index('Permutation', inplace=True)      #set the index to the permutation

        return perm_df

