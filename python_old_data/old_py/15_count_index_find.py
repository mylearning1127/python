#!/usr/bin/python

var="This is python script and it is very easy"

'''

count = checks how many mentioned letters or words are here
index = find the index value of the letter or word. i.e default index value is 0
find = checks the mentioned word is there or not, it is there output will be 0 otherwise output will have valuei
But the mentioned variable must as a first word or letter then only output is 0

'''

print(var.count('python'))
print(var.count('y'))

print(var.index('s'))
print(var.index('s',4))

print(var.find('version'))
print(var.find('This'))
