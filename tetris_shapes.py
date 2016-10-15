xy_plane = [];

def user_input():
	xdim = int(input("Enter x dimension: \n"))
	ydim = int(input("Enter y dimension: \n"))
	while xdim > 20 or ydim > 20:
		print("Dimensions must be below or equal to 20 to render properly.")
		xdim = int(input("Enter x dimension: \n"))
		ydim = int(input("Enter y dimension: \n"))
	init_plane(xdim, ydim)
	#get_coords()
	draw_plane()

def init_plane(xdimension, ydimension):
	for x in range(xdimension+1):
		for y in range(ydimension+1):
			xy_plane.append((x,y,0)) #x,y and whether it is "colored-in"


def get_coords():
	x_coord = int(input("Enter x-coordinate you want found: \n"))
	y_coord = int(input("Enter y-coordinate you want found: \n"))
	xy_coords = xy_plane.index((x_coord, y_coord))
	return(xy_coords)

def draw_plane():
	#Overscore is here: ‾‾
	"""Work on how to draw the shapes"""
	x_limit, y_limit, bin_color = xy_plane[-1]
	print(x_limit, y_limit)
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

user_input()