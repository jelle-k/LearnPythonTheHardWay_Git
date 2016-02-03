# Obtaining data_one; How old am I?
print ("How old are you? "),
age = input()

# Obtaining data_two; How tall am I?
print ("How tall are you? "),
hight = input()

# Obtaining data_three; How much do I weigh?
print ("How much do you weigh? "),
weight = input()

# final statement returns of input data
# replaced %r with %s for hight to get rid of the extra '
print ("So, you're %r old, %s tall and %r heavy." % (
    age, hight, weight))