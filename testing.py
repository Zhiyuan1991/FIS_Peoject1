from utils import *
from dice_state import *

print(euclidean([0,0],[1,1]))

maze=read_maze('puzzle/puzzle2.txt')

print(maze)

print('test dice roll')
start_location=dice(maze,[1,1],1,2,3)
print(start_location.location,start_location.top,start_location.north,start_location.east)
print()

children=start_location.get_children(maze)
for child in children:
	print(child.location,child.top,child.north,child.east)