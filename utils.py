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

def orientation_manhattandistance(locationA, locationB):
	return (abs(locationA[0]-locationB[0])+abs(locationA[1]-locationB[1]))