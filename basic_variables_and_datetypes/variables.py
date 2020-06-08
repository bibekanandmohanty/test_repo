# A variable is nothing but a reserved memory location to store values. In other words a variable in a program giives data to the computer to work on.
# No need to declare varables before using them.
# That is why it is called dynamically typed program.
a=10
b=10.5
print(a)
print(b)

# Dont use quotes around the var name otherwise it will print as it is.
print(type(a))
print(type(b))
#Redeclare a variable
a=23
print(a)
a=10
print(a)
#Delete a variable
del a
#Rules to define a variable
#1. contains letters,numbers and underscore
#2. should not be a keyword like if,print,etc.....
#3. can't contain a space , if u require a space then replace with a underscore
#4. should not start with a number
#5. name of variable is case-sensitive.
#6. can start a variable name with _.