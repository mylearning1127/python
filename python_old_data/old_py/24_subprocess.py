#!/usr/bin/python

import subprocess

#call() function prints output directly, it is not storing output for future

var1=subprocess.call('pwd')

var1=subprocess.Popen(['cat', 'test.p'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = var1.communicate()

print(stdout)

#check_output() function is used to store the output in variable and if we want we can use it in future.

var1=subprocess.check_output('pwd')

print(var1)

subprocess.run('ls')
