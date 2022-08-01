#!/usr/bin/python
import os
import platform

var1=dir(platform)


for v in var1:
  if not v.startswith("_"):
   try:
      print(getattr(platform,v)())
     # print("platform.{}()".format(v))
   except:
      continue	
