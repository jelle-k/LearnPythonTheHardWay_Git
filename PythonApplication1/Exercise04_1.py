#Amount of cars
cars = 100
#How much space there is in the cars
space_in_a_car = 4.0
#How many drivers there are
drivers = 30
#How many passengers there are
passengers = 90
#amount of cars not driven
cars_not_driven = cars - drivers
#amount of drivers there are
cars_driven = drivers
#capacity of all cars totaled
carpool_capacity = cars_driven * space_in_a_car
#Average number of passengers per car
average_passengers_per_car = passengers / cars_driven


#prints number of cars
print ("There are ", cars, " cars available.")
#prints how many cars are availble
print ("There are only ", drivers, " drivers available.")
#prints number of empty cars
print ("There will be ", cars_not_driven, " empty cars today.")
#number of people we can transport
print ("We can transport ", carpool_capacity, " people today.")
#number of passengers to carpool
print ("we have ", passengers, " to carpool today.")
#average number of passengers in each car
print ("We need to put about ", average_passengers_per_car, " in each car.")