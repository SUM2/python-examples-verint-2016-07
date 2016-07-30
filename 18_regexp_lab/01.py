import re
import sys

input_key = sys.argv[1]

with open("config.txt", "r") as config:
    for i in config:
        m = re.search(r'(\w+)\s*=\s*(\w+)', i)
        #if m is not None:
        if m.group(1) == input_key:
            print m.group(2)