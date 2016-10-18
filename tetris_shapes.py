xy_plane = [];

def user_input():
	xdim = int(input("Enter x dimension: \n"))
	ydim = int(input("Enter y dimension: \n"))
	while xdim > 20 or ydim > 20:
		print("Dimensions must be below or equal to 20 to render properly.")
		xdim = int(input("Enter x dimension: \n"))
		ydim = int(input("Enter y dimension: \n"))
	init_plane(xdim, ydim)
	draw_chosen(xdim, ydim)
	draw_graphic_plane(xy_plane)

def init_plane(xdimension, ydimension):
	for x in range(xdimension):
		for y in range(ydimension):
			xy_plane.append((x,y,0)) #x,y and whether it is "colored-in"


def get_coords():
	x_coord = int(input("Enter x-coordinate you want found: \n"))
	y_coord = int(input("Enter y-coordinate you want found: \n"))
	xy_coords = xy_plane.index((x_coord, y_coord))
	return(xy_coords)

def draw_plane():
	#Overscore is here: ‾‾
	x_limit, y_limit, bin_color = xy_plane[-1]
	for i in range(2*x_limit):
		for j in range(y_limit):
			if j != y_limit-1:
				if (i == 0) or (i % 2 == 0):
					print("|‾‾‾", end="")
				elif (i % 2 != 0):
					print("|___", end="")	
			elif j == y_limit-1:
				if (i == 0) or (i % 2 == 0):
					print("|‾‾‾|", end="")
				elif (i % 2 != 0):
					print("|___|", end="")
		print("\r")

def draw_graphic_plane(xy_plane): 
	current_x_value = 0
	for coordinate in xy_plane:
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


def draw_one(): #fills in one grid
	xy_plane[0] = (0, 0, 1)

def draw_all(): #fills all squares
	for coordinate in xy_plane:
		xcoord, ycoord, bcoord = coordinate
		new_coord = (xcoord, ycoord, 1)
		coord_index = xy_plane.index((xcoord, ycoord, bcoord))
		xy_plane.pop(coord_index)
		xy_plane.insert(coord_index, new_coord)

def draw_chosen(xdim, ydim):
	xcoord = int(input("Enter the x-value: \n"))
	ycoord = int(input("Enter the y-value: \n"))
	while xcoord > xdim and ycoord > ydim:
		xcoord = int(input("Enter the x-value: \n"))
		ycoord = int(input("Enter the y-value: \n"))
	new_coord = (xcoord, ycoord, 1)
	coord_index = xy_plane.index((xcoord, ycoord, 0))
	xy_plane.pop(coord_index)
	xy_plane.insert(coord_index, new_coord)

def define_shape(shape, xdim, ydim):
	if shape.lower == "square":
		draw_square(xdim, ydim) 

def draw_square(xdim, ydim):
	#Left-top edge of the square will be marked with a # to show rotation
	pass

user_input()
