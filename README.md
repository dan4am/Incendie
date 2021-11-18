# Description.
This repository contains the code for Incendiary: a simulation of a wild fire.
## Structure:
- [Getting started.](https://github.com/dan4am/Incendie/blob/main/README.md#1-getting-started)
   - [Prerequisites.](https://github.com/dan4am/Incendie/blob/main/README.md#a-prerequesitess)
   - [Run the code.](https://github.com/dan4am/Incendie/blob/main/README.md#b-run-the-code)
   - [The GUI.](https://github.com/dan4am/urubugu/blob/master/README.md#cthe-gui)
   - [Commands.](https://github.com/dan4am/Incendie/blob/main/README.md#d-commands)
   - [Config file.](https://github.com/dan4am/Incendie/blob/main/README.md#e-config-file)
   
## 1. Getting started 
### a. Prerequesites.
- [python 3.9](https://www.python.org/downloads/)
- [pygame 2.0.1](https://www.pygame.org/wiki/GettingStarted)

### b. Run the code.
After downloading and installing python and the necessary libraries, the user have to run the 
following command to play the game:


- On Windows, Unix-like systems and Mac OS:
---
```
python3 main.py 
```
### c. The GUI.
When the code is executed, this pygame window will appear.
![gui](https://user-images.githubusercontent.com/39918471/142399483-127d3cfa-1553-417e-9515-072e5178189e.png)

You can select the cells you want to ignite before the simulation by clicking on them.
They will appear in Red on the GUI
![Selection cells to ignite](https://user-images.githubusercontent.com/39918471/142400391-bd636336-6e6a-4b44-91bc-48a1ee24bc09.png)

You can also select the cells you wish not to ignite by right-clicking on them.
 They Will appear in grey on the GUI.
 
 ![Ashes](https://user-images.githubusercontent.com/39918471/142400802-97a2015c-c6cb-4ca0-b099-f56604aebff2.png)




### d. Commands.

`SPACE` → Start the fire.

`r` → reset the simulation.

`UP` → Increase the speed of the fire.

`DOWN` → Decrease the speed of the fire


### e. Config file.
The config.txt file contains the default settings of the simulations.
The settings are the folowing:
```
Hauteur = 100 (the number of cells in height which is an int value)
```
```
Largeur = 100 (the number of cells in width which is an int value)
```
```
Vitesse = 0.1   (The speed of the fire which has a float value)
```
```
Probabilité = 0.53 (The probability of a cell burning which has a float value)
```

Those values can be changed provided they are the right type (float or int).

The order of the values must not be changed, otherwise the simulation will work in an unpredictable manner.
