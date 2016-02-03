#Amount of cars
x = 100
#How much space there is in the cars
y = 4.0
#How many drivers there are
z = 30
#How many passengers there are
s = 90
#amount of cars not driven
p  = x - z
#amount of drivers there are
t = z
#capacity of all cars totaled
a = p * y
#Average number of passengers per car
g = s / t


#prints number of cars
print ("There are ", x , " cars available.")
#prints how many cars are availble
print ("There are only ", t, " drivers available.")
#prints number of empty cars
print ("There will be ", p, " empty cars today.")
#number of people we can transport
print ("We can transport ", a, " people today.")
#number of passengers to carpool
print ("we have ", s, " to carpool today.")
#average number of passengers in each car
print ("We need to put about ", g, " in each car.")