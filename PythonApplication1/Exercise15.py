from sys import argv

# This sets an argument variable, where in the cmd I will have to type two variables
(script, filename) = argv

# Remember to use "" for the location, and you don't need full file path
txt = open("ex15_sample.txt")

# this will show what the file contains, including the the text document
print ("Here's you file %r:" % filename)
print (txt.read())

# this will ask me to retype the name of the file
print ("I'll also ask you to type it again:")
file_again = input("> ")

# This should re-open the file, however, for me it only states true
txt_again = open(file_again)

# I found out why it was saying true, becasue read --> readable. I was asking, is it readable or not
print (txt_again.read())