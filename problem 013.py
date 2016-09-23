import fileinput
import sys

for line in fileinput.input(['./test.py'], inplace = True):
	sys.stdout.write('nlist.append({l})'.format(l=line))

