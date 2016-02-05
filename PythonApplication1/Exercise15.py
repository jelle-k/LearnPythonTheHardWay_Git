from sys import argv

(script, ex15_sample.txt) = argv

txt = open(ex15_sample.txt)

print ("Here's you file %r:" % ex15_sample.txt)
print (txt.read())

print ("I'll also ask you to type it again:")
file_again = input("> ")

text_again = open(file_again)

print (text_again.readable())