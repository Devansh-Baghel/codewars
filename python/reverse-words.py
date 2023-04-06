# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python


'''
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
Examples

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

def reverse_words(text):
	text = text.split()
	result = []
	for i in text:
		i = i[::-1]
		result.append(i)
	return " ".join(result)
print(reverse_words("This is a test"))