

from random import randint
unknown = randint(1,101)
print unknown

while True:
    s = int(raw_input("Please pick a number\n"))
    cube = randint(1,4) #sometime the user will get "too big"
    if cube == 1:
        print "too BIG;)"
    elif cube == 2:
        print "too SMALL;)" #sometime the user will get "too small"
    elif s > unknown:
        print "too BIG"
    elif s < unknown:
        print "too SMALL"
    else:
        print "You are RIGHT"
        break