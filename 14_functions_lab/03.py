
def mysum(*args):
	total = 0
	for i in args:
		if isinstance (i, int):
			total += (i / 10) % 10
		else:
			return False
	print total