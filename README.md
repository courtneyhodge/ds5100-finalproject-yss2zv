# DS5100 Final Project

## Metadata
**Author:** Courtney Hodge
**Project Name:** Monte Carlo Simulator

## Synopsis

### Brief Demo
> Let's walk through a demo of this final project. Do you want to play a game? Of course you do!

#### Installation
> 1. Install the library into your environment: If you're doing it locally after cloning the repo to your machine, you can call.
```python
pip install .
```
> You can also call the following pip command if it does not work.
```python
pip install Montecarlo
```

#### Import Libraries and Packages
> 2. Import Libraries: Import the necessary libraries to start creating objects.
```python
import numpy as np
import pandas as pd
from montecarlo import Die, Analyzer, Game
```

> 3. Create a coin with faces H and T
```python
coin_array = np.array('H', 'T')
die = Die(coin_array)
```

> 2. Play a Game
from montecarlo_simulator import Game

# Create two dice
die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
die2 = Die(np.array([1, 2, 3, 4, 5, 6]))

# Play a game with the two dice
game = Game([die1, die2])
game.play(10)

> 3. Analyze a Game


## API Description
