import os

def pos(x, y):
	return "\x1b[" + str(y) + ";" + str(x) + 'H'

pnt = lambda x: print(x, end='')


if __name__ == "__main__":
	print("\x1b[2J")

	# print(pos(0,0))
	# print("Hello")
	# print("World")

	pnt(pos(0,0))
	pnt("Left side\n")
	pnt("Of the screen")
	pnt(pos(100,0)+"Right side\n")
	pnt("of the screen")