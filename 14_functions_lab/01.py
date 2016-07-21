
def mysum(*args):
	sum = 0
	for i in args:
		if type(i) == int:
			sum += i
		else:
			print str(i) + " is not an integer"
	print sum

def mymul(*args):
	mul = 1
	for i in args:
		if type(i) == int:
			mul *= i
		else:
			print str(i) + " is not an integer"
	print mul