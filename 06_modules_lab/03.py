
#Search for files that their size is bigger than 1mb and print the name of the file

import os, sys

if len(sys.argv) != 3:
    print "Didn't use properly"
    sys.exit()

search_dir = sys.argv[1]
min_file_size = int(sys.argv[2])

for root,dirs,files in os.walk(search_dir):
    for name in files:
        file_path = os.path.join(root, name)
        file_size = os.path.getsize(file_path)
        if file_size >= min_file_size:
            print "{0} size is {1}. Do you want to delete this ? [y/n] ".format(file_path, file_size)
            answer = raw_input()
            if answer == "y" or "yes":
                print os.remove(file_path)

