# https://www.codewars.com/kata/57e76bc428d6fbc2d500036d

'''
Write a function to split a string and convert it into an array of words.

Examples (Input ==> Output):
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

'''

def string_to_array(s):
	return [""] if s == "" else s.split()

print(string_to_array("This should return an array"))
print(string_to_array("")) # should return [""]