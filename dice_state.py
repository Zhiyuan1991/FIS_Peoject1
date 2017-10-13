#define dice class

import numpy as np
from utils import *

def find_goal_location(maze):
	maze=np.array(maze)
	index=np.where(maze=='G')
	return [index[0][0],index[1][0]]

class dice():
	def __init__(self,maze,location,top,north,east):
		self.location=location
		self.top=top
		self.north=north
		self.east=east
		self.parent=[]
		self.children=[]
		self.key=str(location[0])+str(location[1])+str(top)+str(north)+str(east)
		self.hn=euclidean(self.location,find_goal_location(maze))
		self.gn=0

	def get_children(self,maze):
		children=[]
		max_row=len(maze)
		max_col=len(maze[0])
		offsets=[[1,0],[-1,0],[0,1],[0,-1]]
		for offset in offsets:
			new_row=offset[0]+self.location[0]
			new_col=offset[1]+self.location[1]
			if new_row<0 or new_row>=max_row or new_col<0 or new_col>=max_col:
				continue
			if maze[new_row][new_col]=='*':
				continue
			new_location=[new_row,new_col]
			[top,north,east]=self.roll_dice(offset)
			if top!=6:
				child=dice(maze,new_location,top,north,east)
				child.parent=self
				child.gn=self.gn+1
				children.append(child)
		return children

	def roll_dice(self,offset):
		top=0
		north=0
		east=0
		if offset==[-1,0]:
			top=7-self.north
			north=self.top
			east=self.east
		elif offset==[1,0]:
			top=self.north
			north=7-self.top
			east=self.east
		elif offset==[0,1]:
			top=7-self.east
			north=self.north
			east=self.top
		elif offset==[0,-1]:
			top=self.east
			north=self.north
			east=7-self.top
		else:
			print('unknow offset')
		return [top,north,east]