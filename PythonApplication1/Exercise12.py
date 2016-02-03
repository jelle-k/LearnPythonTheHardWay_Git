# example to remove the new line for promting data
#y = input("name? ")

age = int(input("How old are you? "))
height = int(input("How tall are you? "))
weight = int(input("how much do you weigh? "))

# I replaced with %r with %s to remove '' fom input variables
print ("So, you're %s old, %s tall and %s heavy." % (
    age, height, weight,))