# https://www.codewars.com/kata/56b1f01c247c01db92000076

'''
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "

'''

def double_char(s):
	result = []
	for i in s:
		result.append(i)
		result.append(i)
	return "".join(result)

print(double_char("String"))
print(double_char("Hello World!"))
