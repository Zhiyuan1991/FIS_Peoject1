#define functions

def read_maze(file_name):
	f=open(file_name,'r')
	readLines = f.readlines()
	mazeList = [list(i.strip()) for i in readLines]
	return mazeList

def euclidean(locationA, locationB):
	return ((locationA[0]-locationB[0])**2+(locationA[1]-locationB[1])**2)**0.5

