# DS5100 Final Project

## Metadata
**Author:** Courtney Hodge
**Project Name:** Monte Carlo Simulator

## Synopsis

### Brief Demo
> Let's walk through a demo of this final project. Do you want to play a game? Of course you do!

#### Installation
> If you're doing it locally after cloning the repo to your machine, you can call.
```python
pip install .
```
> Call the following pip command if it does not work.
```python
pip install Montecarlo
```

#### Import Libraries and Packages
> Import the necessary libraries to start creating objects.
```python
import numpy as np
import pandas as pd
from montecarlo import Die, Analyzer, Game
```

### Create a coin (2-sided die)
> The Die class allows you to create Die objects with default weights of 1.0

```python
coin = np.array(['H', 'T'])
die = Die(coin)
```
> Change the weights of one side manually and view its current state

```python
die.update_weight('H', 5.0)
die.die_current_state()
```

> Lastly, you can roll the die a number of times to get a random sample

```python
die.roll()
```

### Play a game

> Create a game object by instantiating a Game object. Below I am playing a game with 5 coins. Calling the play game method flips the coin 10 times. Show the results of the game play by calling the show results method to view a copy of the data frame in either narrow or wide form.

```python
game = Game([die for _ in range(5)])
game.play(10)
game.show_results()
```

### Analyze a Game

> After a game is played, analyze it by instantiating an Analyzer object. View the face values with the respective Analyzer method. View the raw frequency of jackpots by calling Analyzer's jackpot method.

```python
analyzer = Analyzer(game)
analyzer.face_values()
analyzer.jackpot()
```

>Lastly, utilize the combination and permutation Analyzer methods, along with the face_values for further analysis of a game's combination and permutation data frames.

```python
analyzer.combination_count()
```

```python
analyzer.permutation_count()
```
## API Description

### Die

```python
"""Represents a single die with customizable faces."""
```

#### Methods:

```python
__init__(self, faces: np.ndarray, weight: float = 1.0):


"""Initializes the die with a list of faces.
Parameters:
faces (np.ndarray): A NumPy array of unique faces for the die.
weight (float, optional): The initial weight for each face (default is 1.0).
Raises:
TypeError: If faces is not a NumPy array or contains invalid types.
ValueError: If faces do not contain unique values."""
```

```python
update_weight(self, face_value_to_change, new_weight: float):

"""Changes the weight of a specified face.
Parameters:
face_value_to_change (int, float, or str): The face value whose weight is to be changed.
new_weight (int, float, or str): The new weight for the specified face.
Raises:
IndexError: If the face value is not found in the die.
TypeError: If the new weight is not a valid type (int, float, or str)."""
```

```python
roll(self, num_of_rolls: int = 1):

"""Rolls the die a specified number of times.
Parameters:
num_of_rolls (int, optional): The number of times to roll the die (default is 1).
Returns:
list: List of outcomes from the rolls."""
```
```python
die_current_state(self):

"""Returns the DataFrame containing faces and weights.
Returns:
pd.DataFrame: DataFrame containing faces and weights."""
```

### Game
```python
"""Represents a game consisting of multiple dice."""
```
#### Methods:

__init__(self, dice: list):

Initializes a game with a list of dice.
Parameters:
dice (list): List of Die objects.
play(self, rolls: int):

Plays the game by rolling all dice a specified number of times.
Parameters:
rolls (int): Number of times to roll the dice.
show_results(self, form: str = 'wide') -> pd.DataFrame: