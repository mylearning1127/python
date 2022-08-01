#!/usr/bin/python
import sys

var1=dir(sys)

for v in var1:
   if not v.startswith("_"):
     try:
	val=getattr(sys,v)()
	print("{}         : {}".format(v,val))
     except:
	print("This is not applicable: {}".format(v))
