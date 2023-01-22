'''
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

'''

def grow(arr):
	result = 1
	for i in arr:
		result *= i
	return result

print(grow([1,2,3,4]))