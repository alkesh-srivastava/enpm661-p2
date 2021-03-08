## ENPM661 - Path Planning for Autonomous Robot
### Project 2 - Breadth First Search Implementation
### "Testudo on the Hunt"
To run the program you will need to make sure that your *python interpretor* supports the following packages :

* matplotlib	3.3.4	
* numpy	1.20.1	
* pip	21.0.1	
* pygame	2.0.1	

The project consist of the following five files:
1. \_\_main\_\_.py
2. \_\_main_explore\_\_.py
3. configuration.py
4. maze.py
5. myQueue.py

The first two files are the main file that are supposed to be run on your system. The other three files serves the following purposes:

_configuration.py_ - This is the configuration file.that defines the configuration of our maze. In this file, you will find declaration of the possible move sets, definition of obstacle and constraints that will restrict the motion of our player.

_maze.py_ - This file sends the solution to the animation that we will see on running our \_\_main\_\_.py file

_myQueue.py_ -  This python file is Class definition for our datatype Queue. Generating a separate file for class makes the program look clear and easy to understand. For Breadth First Search, Queues are the recommended data structure to be used. List are not very efficient for Queue and therefore we will be using deque. Why? Because deque has popleft() which shakes hand with FIFO notion of Queue.
_\_\_main\_\_.py_ - We will be using pygame to animate the path. We will be using Testudo as our player, #GoTerps! Remember, you will see that Testudo sometimes overlap the border of obstacle. To be honest, it would have been very difficult to let a point object explore the maze. Testudo is a 10x10 sprite and hence the overlap. You can cross check the path (It will be printed in the terminal)

As soon as you will run this program, you will be asked by the terminal to input the x and y coordinate of the input state, and also the x and y co-ordinate of the goal. 



![Entering Co-ordinates](https://github.com/alkesh-umd/enpm661-p2/blob/main/images/1.png)


As soon as you hit enter, the terminal window will print the path that Testudo will take to reach the goal position you desired.




![Print Path](https://github.com/alkesh-umd/enpm661-p2/blob/main/images/2.png)

The animation will begin and testudo will reach its destination, as will be shown in a GIF image soon.

For exploration. you will need to run \_\_main_explore\_\_.py file
Before asking for co-ordinate it will ask the input for Frame per second, which will be the number of frames that you want the animation to render to depict the entire visualization for the path it has taken. I will recommend entering values over 1,000 otherwise it may take forever to explore.




![Frame per second](https://github.com/alkesh-umd/enpm661-p2/blob/main/images/3.png)

After you are done entering the co-ordinates, the terminal will be filled with tuples of co-ordinate and the output my overwhelm your computer system if you have chosen diagonally opposite points.



![Explore](https://github.com/alkesh-umd/enpm661-p2/blob/main/images/4.png)

Thus, with this project we were able to implement Breadth First Search algorithm for a point robot. You will see two animations, whose combined GIF is as :



![GIF](https://github.com/alkesh-umd/enpm661-p2/blob/main/images/6.gif)

At the end of exploration python file, you will get a plot depicting that path our mascot has explored before returning the path calcualted by Breadth First Search.



![Exploration](https://github.com/alkesh-umd/enpm661-p2/blob/main/images/5.png)


You can take the following as random input to test the program :

1. Start (45,54) - Goal (123,213)
2. Start (78,8) - Goal (213,213)
3. Start (45,90) - Goal (12,12)


If you suffer any issue running the program, please contact :
Alkesh Srivastava
(alkesh@umd.edu)


