import numpy as np


class dice_state():
	def __init__(self,grid,location,top,north,east):
		self.location=location
		self.top=top
		self.north=north
		self.east=east
		self.parent=[]
		self.children=self.get_children(grid)
	
	def get_children(self,grid):

		
	def 