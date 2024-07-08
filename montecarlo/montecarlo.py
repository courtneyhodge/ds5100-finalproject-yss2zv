import numpy as np
import pandas as pd

class Die():
    def __init__(self, faces, weight = 1.0):                        #W defualts to 1.0
        '''
        Takes a NumPy array of faces as an argument. Throws 
        a TypeError if not a NumPy array. The array’s data 
        type dtype may be strings or numbers. The array’s 
        values must be distinct. Tests to see if the values 
        are distinct and raises a ValueError if not. Internally 
        initializes the weights to  1.0 for each face.
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
            print("Faces are all ints!")

        elif np.issubdtype(faces.dtype, np.floating):               #check if sub dtypes of faces are floats
            print("Float faces are now all floats!")

        elif np.issubdtype(faces.dtype, np.str_):                   #check if sub dtypes of faces are str
            for element in faces:                                   #if so, try to change them to ints
                try:
                    int(element)   
                except:
                    raise TypeError("wrong type: all faces must be strings or numbers") #if there's a TypeError, raise it
            print("String faces are now all ints!")
            
        else:
            raise TypeError("wrong type: all faces must be strings or numbers") #if none of the above, raise TypeError

        if(len(np.unique(faces)) != len(faces)):                    #check if each value is unique in faces, if not, raise ValueError
            raise ValueError("duplicate values: faces must be distinct")
        else:
            print("Faces are all unique!")

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
        Takes two arguments: the face value to be changed and the new weight,
        checks to see if the face passed is valid value, i.e. if it is in the die array. 
        If not, raises an IndexError. Checks to see if the weight is a valid type,
        i.e. if it is numeric (integer or float) or castable as numeric. If not, raises a TypeError.
        Updates the weights of the die.
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
            
            
    def roll(self, num_of_rolls = 1):
        '''
        This is essentially a random sample with replacement, from the
        private die data frame, that applies the weights.
        Returns a Python list of outcomes.
        Does not store internally these results.
        '''

        return self._private_data_frame.sample(n = num_of_rolls, replace = True,             #convert the df to a list as specified
                                               weights = self.weight).faces.tolist()


    def die_current_state(self):  
        '''
        Returns a copy of the private die data frame.
        '''
        return self._private_data_frame.copy()
        
    
    
class Game():
    def __init__(self, dice_list):
        '''
        Takes a single parameter, a list of already instantiated similar
        dice.
        '''
        if all(isinstance(die, Die) for die in dice_list):                 #check if all objects in dice_list are instances of Die
            self.dice_list = dice_list                                     #if so, set self.dice_list to dice_list
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
        '''
        result_dict = {f'Die_{i}': [] for i in range(len(self.dice_list))} #create a dictionary to store the results in

        for i in range(num_rolls):                                         #roll the dice num_rolls times
            for j, die in enumerate(self.dice_list):                       #roll each die in the list
                result_dict[f'Die_{j}'].append(die.roll())                 #append the result of the roll to the dictionary

        self._private_data_frame_2 = pd.DataFrame(result_dict)             #save the results in a private data frame
        self._private_data_frame_2.index.name = "Roll Number"              #set the index name to "Roll Number"
                
    def show_results(self, wide_or_narrow = "wide"):
        '''
        This method just returns a copy of the private play data frame to
        the user. Takes a parameter to return the data frame in narrow or 
        wide form which defaults to wide form. The narrow form will have 
        a MultiIndex, comprising the roll number and the die number 
        (in that order), and a single column with the outcomes (i.e. the 
        face rolled). This method should raise a ValueError if the user 
        passes an invalid option for narrow or wide. 
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
    def __init__(self):
        pass
    