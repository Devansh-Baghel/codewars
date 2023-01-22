'''
After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).

'''

def rental_car_cost(d):
	cost = 0
	for day in range(d):
		cost += 40
	if d >= 7:
		cost -= 50
	elif d >= 3:
		cost -= 20
	return cost


print(rental_car_cost(0))
print(rental_car_cost(1))
print(rental_car_cost(2))
print(rental_car_cost(3))
print(rental_car_cost(4))
print(rental_car_cost(6))
print(rental_car_cost(7))
print(rental_car_cost(9))