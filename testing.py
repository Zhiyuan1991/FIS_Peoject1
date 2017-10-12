from utils import *
from dice_state import *

print('test dice roll')
maze=read_maze('puzzle/puzzle0.txt')
print('start')
start_location=dice(maze,[0,0],1,2,3)
start_location.display_path(maze)
print(start_location.location,start_location.top,start_location.north,start_location.east)
print('children')
children=start_location.get_children(maze)
for child in children:
	print(child.location,child.top,child.north,child.east)


#main
print('main')

maze=read_maze('puzzle/puzzle0.txt')
goal_location=find_goal_location(maze)
print('Goal location: ',goal_location)
start_location.display_path(maze)
start_location=dice(maze,[0,0],1,2,3)

visited=list()
queue=list()

queue.append(start_location)

flag=0
result=0

while queue:
	queue=sorted(queue, key=lambda dice: dice.hn+dice.gn,reverse=True)
	node=queue.pop()
	print("this node: ",node.top,node.location,node)
	if node.key in visited:
		continue
	visited.append(node.key)
	if node.location==goal_location and node.top==1:
		flag=1
		result=node
		break
	children=node.get_children(maze)
	print(children)
	print("this node children:",len(children))
	for child in children:
		queue.append(child)

if flag==1:
	print("solution found")
	print('maze:')
	print(maze)
	for line in maze:
			print(line)
	path=[result]
	cur=result
	while cur.parent:
		path.append(cur.parent)
		cur=cur.parent
	path=path[::-1]
	for node in path:
		print()
		node.display_path(maze)
else:
	print('Solution failed')

