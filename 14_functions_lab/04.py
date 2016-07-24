def longer_than(num,*args):
	lst = []
	for i in args:
		if len(i) > num:
			lst.append(i)
	return lst