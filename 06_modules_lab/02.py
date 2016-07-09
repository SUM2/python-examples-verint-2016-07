
#print the sum of 2 numbers within sys.argv

import sys
if len(sys.argv) != 3:
    print "Please enter 2 numbers !"

num1 = sys.argv[1]
num2 = sys.argv[2]
print (num1 + num2)