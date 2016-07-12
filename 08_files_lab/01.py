
#a program that gets 2 file's name and add
# the content of the first file to the second


import os, sys

if len(sys.argv) != 3:
    print "Please insert 2 file's name"
    sys.exit()

(_, file1, file2) = sys.argv

with open(file1, "r") as fout:
    with open(file2, "a") as fin:
        for line in fout:
            fin.write(line)

