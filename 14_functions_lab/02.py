

def values(number, string):
	if type(number) == int and type(string) == str:
		return True
	else:
		raise Exception("First value should be number and second a string")
			