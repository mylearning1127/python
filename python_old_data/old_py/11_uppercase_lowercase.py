#!/usr/bin/python

'''
	upper - All the string in uppercase
	lower - All the string in lowercase
        title - Every first letter in the string is upper
	casefold - all the letter in string is lower
        capitalize - first letter on the compltete line is upper
'''

var1="python scripting"

print(var1.lower())

print(var1.upper())

print(var1.title())

value1=var1[0:6].lower()
value2=var1[7:17].upper()
print " "
print("{} {}".format(value1,value2))

