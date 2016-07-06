sum = 0
for i in range(8):
    from random import randint
    sum += randint(1, 101)
print sum

if sum % 7 == 0:
    print "Boom"

