# to run this file, either click on it in the folder system or type in the terminal 'python <filename>'
# or 'python3 <filename>' (depending on system default. Try to always use python 3.x, as version
# 2.7 will be discontinued soon. This file is written for python 3.x 

# Import the numpy library as 'np', which you use to access its routines
import numpy as np
import matplotlib.pyplot as plt  # plotting environment. Borrows stuff from matlab. VERY GOOD.

# NOTE: DO NOT MIX TABS AND SPACES IN PYTHON. USE SPACES ALWAYS.

filename='tracks.txt'

# Variables can be assigned without declaration,
# if you assign to a new type then the variable becomes that type
x=5        #integer
x=5.0      #float
x='hello'  #string

y = [1, 2, 3]  # a list, python's default array object
x=y # x becomes a pointer to y, so if y changes, then x will change

z = np.array([1, 2, 3])  # the numpy array object. much better for maths than lists.
                         # lookup numpy documentation for lots of fancy array operations
			
# some stuff numpy arrays can do:
z += 1  # add one to every element
z *= 2  # multiply all elements by 2
# look up more stuff!!
			
z = np.array(y)  # construct an array from a python list

# Load the file with default settings as a numpy array
# please lookup this documentation
# Numpy routines will ALWAYS use/store stuff in numpy arrays
data = np.loadtxt(filename)

print(data)

# In python there is no 'endif' or 'enddo'
# for functions you can 'return' stuff, but
# if you don't need to return anything then
# you can leave it out completely. Functions
# and if/do/while statements are delimited by 
# indentation.

for i in [1,2,3]:
	print(i)
	
loop=True  # booleans
loop=False
	
if loop==False:
	print('This is an if statement')
	
# a function. There are no subroutines in python, 
# but a function can return many things (or nothing)
# so they act as both functions and subroutines.
def function_name(a,b,c):
	# Pass in arguments a,b,c. Outputs don't need to
	# go in the arguments list.
	print('Function activated')
	
	a = b + c
	
	return a
# you don't even have to return. the indentation level will
# tell python the function has ended	
