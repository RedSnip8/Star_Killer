# Star Killer

Code written by [Frank Cipolone aka RedSnip8.](https://github.com/RedSnip8)


### Index
* [Overview](#overview)
* [Desription of Code Function](#code-function)
* [Getting Started](#getting-started)
* [How to Play](#how-to)


## <a name="overview"></a>Overview
Star Killer is a experimental ship used by the Space Force troops stationed on the Moon. Star Killer is powered with an AI that is able to learn and adapt to it enviornments. It is designed to gather intel on enemies durign engagments, self-repair, and self-upgrade based on the needs of a situation.  You are out on a training run to train the Star Killer AI, when suddenly an unkown force attacks. Alone, you must face down the Unknown force and survive to warn the home base.

## <a name="code-function"></a>Description of Code Function
In Star Killer the player will control a ship on the right side of the screen. They wil be able to speed up, slow down, and manuver up and down using the arrow keys. When the game begins a fleet of enemies will appear and begin to attack the player and move to the left of the screen. The player will have to shoot and try to destroy the enemy ships. The ships shields will be able to absorb some damage, but it will eventually fail and leave the player exposed after too much damage is taken. The player will have to wait for the shield generator to recharge. For every ship the player destroys they will gain intel and the ship will adapt to the threat better. If the player is destroyed they will lose the game and be brought back to the home screen.

The game will track all of the destroyed enemies and gain intel points for each enemy. You can simply survive the allotted time or try to gather intel on all the enemy ships before time runs out. For each full intel piece a new upgrade to the ship will also be added. 

The is a power managment system that will add a layer of difficulty to the game. Using boosters, firing lasers, using experimental weapons, and charging your shields will drain power to the ship.

## <a name="getting-started"></a>Getting Started:


### System Requirements
This code is meant to run on either Ubuntu 16.04 or Ubuntu 18.04 with Pygame 1.9.5 and Python 3.6.7. 

#### Getting Python 3 and Pygame
Start by updating the package list:
```
sudo apt-get update
```

Install Python 3
```
sudo apt-get install python3
```

Install pip3
```
sudo apt install python3-pip
```

Verify python3 and pip3 are installed with the correct versions
```
python3 --version && pip3 --version

_sample output_
Python 3.6.7
pip 19.0.3 from /usr/local/lib/python3.6/dist-packages/pip (python 3.6)
```

Install Pygame
```
pip3 install --user pygame
```

## <a name="how-to"></a>How to Play

Basic Controls
* Up = Arrow Up
* Down = Arrow Down
* Boost = Space
* Shoot = v

You can increase power to your thrusters by using the spacebar. Boosting your thrusters will drain power faster that you can replish. Since all of your systems run on the same power source,  be sure to manage your power consumption and save the boost for emergencies.