import math
import sys
import os

print("Hello World")

print(2**2)


xx = 5
yy = "7"

print(xx + int(yy))
print(str(xx) + yy)


for arg in sys.argv:
    print(arg)

print(sys.platform)

print(sys.version_info)

print(os.getpid())

print(os.getcwd())

print(os.getlogin())

x = 10
y = 2.24552
z = "I like turtles!"

print(f"x is {x}, y is {y}, z is {z}")

xxx = [1, 2, 3]
yyy = [8, 9, 10]

xxx.append(4)
print(xxx)

for i in range(0, len(yyy)):
    xxx.append(yyy[i])

print(xxx)
del xxx[4]
print(xxx)
xxx.insert(5, 99)
print(xxx)

print(len(xxx))


xxxx = [i * 1000 for i in xxx]
print(xxxx)


"""
Python tuples are sort of like lists, except they're immutable and
are usually used to hold heterogenous data, as opposed to lists
which are typically used to hold homogenous data. Tuples use 
parens instead of square brackets. 
More specifically, tuples are faster than lists. If you're looking
to just define a constant set of values and that set of values 
never needs to be mutated, use a tuple instead of a list. 
Additionally, your code will be safer if you opt to "write-protect"
data that does not need to be changed. Tuples enforce immutability
automatically. 
"""
# Example:


def dist(a, b):
    """Compute the distance between two x,y points."""
    x0, y0 = a  # Destructuring assignment
    x1, y1 = b

    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)


a = (2, 7)   # <-- x,y coordinates stored in tuples
b = (-14, 72)

# Prints "Distance is 66.94"
print("Distance is: {:.2f}".format(dist(a, b)))


# Write a function `print_tuple` that prints all the values in a tuple

# YOUR CODE HERE

def print_tuple(isaTuple):
    for i in isaTuple:
        print(i)


t = (1, 2, 5, 7, 99)
print_tuple(t)  # Prints 1 2 5 7 99, one per line

# Declare a tuple of 1 element then print it
u = (1)  # What needs to be added to make this work?
print_tuple(f"{u}")
