
lst = map(chr, range(ord('a'), ord('z')+1))
print [x + y + z for x in lst for y in lst for z in lst]
