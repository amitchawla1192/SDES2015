from text_plot import *
def test_plot():
	x = []
	y = []
	import math
	no_points = 30
	for i in range(no_points):
		y.append(2 * (math.pi/no_points)*i)
		x.append(math.sin(y[i]))
#	print x,y
	plot(x,y,30,80)

if __name__ == '__main__':
	test_plot()
	
