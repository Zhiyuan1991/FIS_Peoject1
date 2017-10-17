#define functions

import copy

def read_maze(file_name):
	f=open(file_name,'r')
	readLines = f.readlines()
	mazeList = [list(i.strip()) for i in readLines]
	return mazeList

def display_maze(maze, dice=None):
	maze_copy=copy.deepcopy(maze)
	if dice:
		location=dice.location
		maze_copy[location[0]][location[1]]=str(dice.top)
	for line in maze_copy:
		print(line)

def euclidean(locationA, locationB):
	return ((locationA[0]-locationB[0])**2+(locationA[1]-locationB[1])**2)**0.5

def manhattan_distance(locationA, locationB):
	return (abs(locationA[0]-locationB[0])+abs(locationA[1]-locationB[1]))


#define functions
import math

import copy

def read_maze(file_name):
	f=open(file_name,'r')
	readLines = f.readlines()
	mazeList = [list(i.strip()) for i in readLines]
	return mazeList

def display_maze(maze, dice=None):
	maze_copy=copy.deepcopy(maze)
	if dice:
		location=dice.location
		maze_copy[location[0]][location[1]]=str(dice.top)
	for line in maze_copy:
		print(line)

def euclidean(locationA, locationB):
	return ((locationA[0]-locationB[0])**2+(locationA[1]-locationB[1])**2)**0.5

def manhattan_distance(locationA, locationB):
	return (abs(locationA[0]-locationB[0])+abs(locationA[1]-locationB[1]))


def orientation_manhattan_distance(locationA, locationB,currenttop,goaltop):
    current_x, current_y = locationA[0], locationA[1]
    goal_x, goal_y = locationB[0], locationB[1]


    x_steps, y_steps = abs(goal_x - current_x), math.fabs(goal_y - current_y)
    is_target_goal_top = (currenttop - goaltop) == (x_steps + y_steps) % 4
    manhattan = manhattan_distance(locationA, locationB)

    if x_steps == 0 and y_steps == 0 and is_target_goal_top: # Case 1: on the goal state and in correct configuration
        return manhattan # we can have here 0 as well. Same thing

    if x_steps == 0 and y_steps == 0 and not is_target_goal_top: #Case 2: on the goal state but in wrong configuration. Need four more steps to be case 1.
        return 4

    if x_steps == 0 and y_steps > 0 and is_target_goal_top: #Case 3: in line with goal state in vertical direction with goal state configuration on top. Now one can rotate in right/left direction, make y_steps moves and reverse rotate it.
        return manhattan + 2

    if x_steps > 0 and y_steps == 0 and is_target_goal_top: #Case 4: in line with goal state in horizontal direction with goal state configuration on top. Now one can rotate in up/down direction, make x_steps moves and reverse rotate it.
        return manhattan + 2

    if x_steps > 0 and y_steps > 0 and is_target_goal_top: # [1, inf), [1, inf), 0
        return manhattan

    if x_steps > 0 and y_steps > 0 and not is_target_goal_top: # [1, inf), [1, inf), 1
        return manhattan +4

    return manhattan # default to manhattan


