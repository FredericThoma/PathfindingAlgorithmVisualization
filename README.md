# PathfindingAlgorithmVisualization

Small hobby-project written in python, pygame was used for the GUI.
The user can create a maze either manually or automatically. He can then choose one of the implemented algorithms. After the solving process has been started, each step the algorithm does is drawn to a pygame window. After completion the user sees whether or not a path to the target node was found and how many steps it took the algorithm to solve the maze.

![alt text](https://github.com/FredericThoma/PathfindingAlgorithmVisualization/blob/main/images/screenshots/s2.PNG)

In order to try the tool yourself:
1. Clone repo or download zip
2. install requirements:
  - pip install -r requirements.txt
  
  OR
  - pip install pygame
3. run main.py

Implementation details:

First of all it should be noted that diagonal steps are allowed, they are 1.4x as expensive as straight steps though.
All implemented algorithms are guaranteed to find the optimal path (if it exists). However, since Breadth-First-Search is unweighted it treats diagonal steps the same as straight steps.

The following algorithms were added so far:

1. A* (https://en.wikipedia.org/wiki/A*_search_algorithm)
2. Dijkstras Algorithm (https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
3. Breadth-First-Search (https://en.wikipedia.org/wiki/Breadth-first_search)

For the automatic maze-generation the cellular automaton B3/S1234 was used. (https://en.wikipedia.org/wiki/Maze_generation_algorithm#Cellular_automaton_algorithms)

In case you are wondering why this particular method was used instead of a randomized iterative or recursive approach, let's look at the pros and cons:

CONS (opposed to most other methods)
1. final maze is predetermined by the starting state => predictable, repeating patterns
2. solvability cannot be insured
3. no trivial break condition => unneccessary work


PROS:
1. it looks pretty cool

So clearly there wasn't much of a choice.
