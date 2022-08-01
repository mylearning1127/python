#!/usr/bin/python
import platform

var1=dir(platform)

for v in var1:
   var2=v[0]
   if var2 != "_":
     try:
	val=getattr(platform,v)()
	print("{} : {}".format(v,val))
     except:
	print("Not applicable: {}".format(v))
