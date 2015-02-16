def plot(x,y,size_x = 30,size_y = 80):
	"""plot(x,y,size_x,size_y) where size_x default is 30 and size_y default is 80"""
	if(len(x) != len(y)):
		raise ValueError ("Both lists are not of same size")	# To check if both lists are of same size
	string = []
	for i in range(size_x):						# Creating initaial list comprising of spaces and new lines
              for j in range(size_y):
                   string.append(' ')
              string.append('\n')
#	print len(string)
	x_new = []
	y_new = []
	x_min = min(x)
	y_min = min(y)
	if x_min >= 0:							# if no negative numbers in list no need to shift
		x_min = 0
	if y_min >= 0:
		y_min = 0
	for i in range(len(y)):
		y_new.append(y[i]-y_min)
		x_new.append(x[i]-x_min)
	x_new_max = max(x_new)
	y_new_max = max(y_new)
        for m in range(len(x)):
		if x_new_max > 0 :
			x_new[m] = int(round(float(x_new[m])*(size_x-1)/x_new_max))	# scaling according to lists range
		else: 
			x_new[m] = int(x_new[m])
		if y_new_max > 0 : 
			y_new[m] = int(round(float(y_new[m])*(size_y-1)/y_new_max))
		else:
			y_new = int(y_new[m])

		string[x_new[m]*(size_y+1)+y_new[m]] = '*'					# replacing required spaces with '*'

	graph = ''
	for i in reversed(range(size_x)):			# reversing string row wise so as to print on string as standard notion
		graph = graph + ''.join(string[i*(size_y+1):(i+1)*(size_y+1)])			
	print graph

def test_plot():
#	x = [-3.5,1,4.5,10.18,25]
#	y = [-15,5.2,60,25.43,64]
	x = [1,2,7,5,79]
	y = [2,3,5,6,29]
	plot(x,y)

if __name__ == '__main__':
	test_plot()
							

