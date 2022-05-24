''' 1. Print the cli arguments count
e.g. python test.py arg1 arg2 arg3
2. Print the cli arguments list python test.py arg1 arg2 arg3
3. Get cli string argument and concatenate'''


import sys
arguments = sys.argv
print ( f"{arguments[0]} {arguments[1]} {arguments[2]} {arguments[3]}")
str = ''.join(arguments)
print ( str )

