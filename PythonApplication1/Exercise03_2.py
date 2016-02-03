#Imports
import math
import reprlib
import formatter

#--------------------
#Floats calculations
#--------------------
print (3602879701896397 / 2 ** 55)

print (1 / 10)

print (str(math.pi))

print (repr(math.pi))

print (format(math.pi, '.2f'))

print (.1 + .1 + .1 == 0.3)

print (round(.1, 1) + round(.1, 1) + round(.1, 1) == round(.3, 1))

print (round (.1 + .1 + .1, 10) == round (.3, 10))
