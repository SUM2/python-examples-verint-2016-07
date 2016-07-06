
from random import randint
number = randint(1,10001)
numberstr = str(number)

sum = 0
for i in numberstr:
    sum += int(i)

print numberstr
print sum



