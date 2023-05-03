# https://www.codewars.com/kata/57eae65a4321032ce000002d

'''
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string

'''

def fake_bin(x):
	result = ''
	for i in x:
		if int(i) < 5:
			result += "0"
		else:
			result += "1"
	return result

print(fake_bin("981324510351938457"))
print(fake_bin("9823453464623"))