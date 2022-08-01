#!/usr/bin/python
'''

"is" and "is not" are identity operators
"in"and "not" are membership variable

'''
var1="test"
var2="test"

if var1 is var2:
	print("var1 and var2 is equal")
else:
	print("var1 and var2 is not equal")

print(var1 is not var2)

value=[1.1,1.2,1.3,1.4]

x= 1.2

if x in value:

	print("Available")
else:
	print("Is not available")

if x not in value:
	print("Available")
else:
        print("Is not available")

