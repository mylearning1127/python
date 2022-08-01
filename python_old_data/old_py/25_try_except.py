#!/usr/bin/python

import platform

var1=dir(platform)

for fun in var1:
  if not fun.startswith("_"):
   try:
     print(getattr(platform,fun)()) 
   except:
     print("Not applicable: {}".format(fun))
