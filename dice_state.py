#define dice class and A* algorithm

import numpy as np
from utils import *

class dice():
	def __init__(self,maze,location,top,north,east):
		self.location=location #current location, row and col
		self.top=top
		self.north=north
		self.east=east
		self.parent=[]
		self.children=[]
		self.key="r"+str(location[0])+"c"+str(location[1])+"t"+str(top)+"n"+str(north)+"e"+str(east)
		self.hn=[] #heuristic function list
		self.hn.append(euclidean(self.location,find_goal_location(maze)))
		self.hn.append(manhattan_distance(self.location,find_goal_location(maze)))
		self.hn.append(orientation_manhattan_distance(self.location,
			find_goal_location(maze),
			self.top,
			1
			))
		self.gn=0

	def get_children(self,maze): #compute next possible moves
		children=[]
		max_row=len(maze)
		max_col=len(maze[0])
		offsets=[[1,0],[-1,0],[0,1],[0,-1]]
		for offset in offsets:
			new_row=offset[0]+self.location[0]
			new_col=offset[1]+self.location[1]
			if new_row<0 or new_row>=max_row or new_col<0 or new_col>=max_col:
				continue
			if maze[new_row][new_col]=='*': # if next location is an obstacle, continue
				continue
			new_location=[new_row,new_col]
			[top,north,east]=self.roll_dice(offset) #get the driection of dice in the new location
			if top!=6:
				child=dice(maze,new_location,top,north,east)
				child.parent=self
				child.gn=self.gn+1 #update cost
				children.append(child)
		return children

	def roll_dice(self,offset): #roll dice in four directions.
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

def rolling_dice(maze,function_number): # A* search
	print()
	start_location=find_start_location(maze) #find start location
	goal_location=find_goal_location(maze) #find goal location
	
	start_dice=dice(maze,start_location,1,2,3) #initialize start dice

	visited=dict()
	queue=list()

	queue.append(start_dice)

	#set up cost for three heuristic functions
	if function_number==0:
		print('------- method '+str(function_number+1)+': euclidean -------')
		visited[start_dice.key]=start_dice.hn[0]
	elif function_number==1:
		print('------- method '+str(function_number+1)+': manhattan -------')
		visited[start_dice.key]=start_dice.hn[1]
	elif function_number==2:
		print('------- method '+str(function_number+1)+': orientation_manhattan -------')
		visited[start_dice.key]=start_dice.hn[2]

	flag=0 #find-result flag
	result=0

	nodes_count=1
	visited_count=0

	while queue:
		#find minimun cost dice
		queue=sorted(queue, key=lambda dice: dice.hn[function_number]+dice.gn,reverse=True)
		node=queue.pop() #pop it from queue
		visited_count+=1
		if node.location==goal_location and node.top==1: #goal found
			flag=1
			result=node
			break
		children=node.get_children(maze)
		all_keys=visited.keys()
		flag_better=0
		#update queue and cost
		for child in children:
			if child.key not in all_keys:
				flag_better=1
			elif child.hn[function_number]+child.gn<visited[child.key]:
				flag_better=1
			else:
				flag_better=0
			if flag_better==1:
				visited[child.key]=child.hn[function_number]+child.gn
				queue.append(child)
				nodes_count+=1

	step_count=-1
	if flag==1: #find result
		print("solution found!")
		print('initial maze:')
		display_maze(maze)
		path=[result]
		cur=result
		while cur.parent:
			path.append(cur.parent)
			cur=cur.parent
		path=path[::-1]
		for node in path:
			print()
			step_count+=1
			print('step: '+str(step_count))
			display_maze(maze,node)
			print('dice state: ','{',node.top,node.north,node.east,node.location[0],node.location[1],'}')
		print()
		print('dice state description: {top,north,east,row,col}')	
	else: #not find result
		print('Solution failed!')
	print()
	print('nodes generated: ',nodes_count)
	print('nodes visited: ',visited_count)
	print('steps: ', step_count)
	print('------- method '+str(function_number+1)+': ends -------')
	return nodes_count,visited_count