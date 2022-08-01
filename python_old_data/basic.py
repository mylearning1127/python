#!/usr/bin/python3

'''
This is helpful to mention multi line comments.
whatever mentioned here will treat as commented line
'''

# variable declaration
name = "suthan"
age = 24
Employee = True
company = "LTI"

# Multi IF, Nested If conditions
if ( age >= 18 and name == "suthan"):                                        # Multi Expression in single IF statment
        if Employee:                                                         # Nested IF statement
           print ("{} is an employee in {}".format(name,company))            # Variable calling in print
elif Employee:
    print ("he is an Employee")                                 
else:
    print ("Nothing mentioned")                                              # Teted working fine till Now

# Functions in python
def details():                                                               # Global variable used
    if (name == "suthan"):
        print ("Hi  " + name)
        if (age >= 18):
            print ("You're an adult")
details()

def details1(name="suthan",age=19):                                          # Function defined variable used
    if (name == "suthan"):
        print ("Hi  " + name + " second statement")
        if (age >= 18):
            print ("You're an adult")
details1()

def details2(name="suthan",age=19):                                          # Function calling variable used
    if (name == "suthan"):
        print ("Hi  " + name + " Thrid statement")
        if (age >= 18):
            print ("You're an adult")
details2("suthakar",21)

def returnvalue():
    return  "Hi {}, now you are on {} years old".format(name,age)            # Storing output function into return value
return_value = returnvalue()
print (return_value)
