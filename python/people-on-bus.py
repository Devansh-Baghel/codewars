'''
There is a bus moving in the city, and it takes and drop some people in each bus stop.

You are provided with a list (or array) of integer pairs. Elements of each pair represent number of people get into bus (The first item) and number of people get off the bus (The second item) in a bus stop.

Your task is to return number of people who are still in the bus after the last bus station (after the last array). Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there :D

Take a look on the test cases.

Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return integer can't be negative.

The second value in the first integer array is 0, since the bus is empty in the first bus stop.
'''

def number(bus_stops):
	people_entered = 0
	people_exited = 0
	for bus_stop in bus_stops:
		people_entered += bus_stop[0]
		people_exited += bus_stop[1]
	return people_entered - people_exited

print(number([[10,0],[3,5],[5,8]]))    # 5
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))    # 17
print(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]))    # 21