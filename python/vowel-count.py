'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
'''

def get_count(sentence):
	vowels = ["a","e","i","o","u"]
	count = 0
	for letter in sentence:
		if letter in vowels:
			count += 1
	return count

print(get_count("iyagsefhsdbfj"))
print(get_count("devansh"))
print(get_count("baghel"))
print(get_count("aeiou"))