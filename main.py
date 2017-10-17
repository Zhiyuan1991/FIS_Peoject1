#main function 

from utils import *
from dice_state import *
import sys

import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv)<2:
	print("usage: python main.py [maze.txt]")
	exit()
maze=read_maze(sys.argv[1])
print('maze: ')
display_maze(maze)

generated1,visited1=rolling_dice(maze,0) #for method 1
generated2,visited2=rolling_dice(maze,1) #for method 2
generated3,visited3=rolling_dice(maze,2) #for method 3

#draw the bar 
# data to plot
n_groups = 3
generated = (generated1,generated2,generated3)
visited = (visited1,visited2,visited3)
 
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, generated, bar_width,
                 alpha=opacity,
                 color='b',
                 label='generated')
 
rects2 = plt.bar(index + bar_width, visited, bar_width,
                 alpha=opacity,
                 color='g',
                 label='visited')
 
plt.xlabel('Methods')
plt.ylabel('Count')
plt.title('Performance metrics')
plt.xticks(index + bar_width, ('euclidean', 'manhattan', 'orientation_manhattan'))
plt.legend()
 
plt.tight_layout()
#plt.show()