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
    def __init__(self, list_of_instantiated_die):
        pass
    
    
class Analyzer():
    def __init__(self):
        pass
    