class Rectangle:
	def __init__(self, x, plane):
		self.x = x
		self.y = x
		self.xy_plane = plane
		self.user_input()
		self.draw_shape_chosen()
		self.draw_graphic_plane()

	def user_input(self):
		while True:
			xdim = int(input("Enter x dimension: \n"))
			ydim = int(input("Enter y dimension: \n"))
			if xdim < 20 and ydim < 20:
				break
			print("Both dimensions must be smaller than 20 to render properly.")
		self.init_plane(xdim, ydim)

	

	def init_plane(self, xdimension, ydimension):
		for x in range(xdimension):
			for y in range(ydimension):
				self.xy_plane.append((x,y,0)) #x,y and whether it is "colored-in"

	def draw_one_chosen(self, coord_capsule):
		x_coord, y_coord, b_coord = coord_capsule
		new_coord = (x_coord, y_coord, 1)
		coord_index = self.xy_plane.index((x_coord, y_coord, 0))
		self.xy_plane.pop(coord_index)
		self.xy_plane.insert(coord_index, new_coord)


	def draw_shape_chosen(self):
		for ycoord in range(self.y):
			for xcoord in range(self.x):
				coord_capsule = (xcoord, ycoord, 0)
				self.draw_one_chosen(coord_capsule)

	def draw_graphic_plane(self): 
		current_x_value = 0
		for coordinate in self.xy_plane:
			xcoord, ycoord, bincoord = coordinate
			if xcoord != current_x_value:
				print("\r")
				current_x_value = xcoord
				if bincoord == 0:
					print("|‾‾", end="")
				elif bincoord == 1:
					print("|##", end="")
			else:
				if bincoord == 0:
					print("|‾‾", end="")
				elif bincoord == 1:
					print("|##", end="")
				current_x_value = xcoord
		print("\n")

	def draw_all(self): #fills all squares
		for coordinate in self.xy_plane:
			xcoord, ycoord, bcoord = coordinate
			new_coord = (xcoord, ycoord, 1)
			coord_index = self.xy_plane.index((xcoord, ycoord, bcoord))
			self.xy_plane.pop(coord_index)
			self.xy_plane.insert(coord_index, new_coord)

	def clear_all(self): #fills all squares
		for coordinate in self.xy_plane:
			xcoord, ycoord, bcoord = coordinate
			new_coord = (xcoord, ycoord, 1)
			coord_index = self.xy_plane.index((xcoord, ycoord, bcoord))
			self.xy_plane.pop(coord_index)
			self.xy_plane.insert(coord_index, new_coord)

	def get_coords(self):
		x_coord = int(input("Enter x-coordinate you want found: \n"))
		y_coord = int(input("Enter y-coordinate you want found: \n"))
		xy_coords = self.xy_plane.index((x_coord, y_coord))
		return(xy_coords)
