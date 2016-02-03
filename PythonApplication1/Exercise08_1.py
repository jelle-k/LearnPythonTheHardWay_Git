import formatter

#Don't forget to import formatter
formatter = ("%r %r %r %r")

#With out ""
print (formatter % (1, 2, 3, 4))

print (formatter % ("One", "Two", "Three", "Four"))

#this will repeat r% r% r% r%
print (formatter % (formatter, formatter, formatter, formatter, ))

#I had forgotten to add commas
print (formatter % (
    "If had this thing.",
    "That you ccould type up right.",
    "But it didn't sing.",
    "So I said goodnight.", 
    )
)