
import sys

if len(sys.argv) != 2:
    sys.exit("Please enter only one number")

number = int(sys.argv[1])

for i in range (number):
    print "hello python"