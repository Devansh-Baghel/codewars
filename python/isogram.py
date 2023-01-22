'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false

'''

def is_isogram(string):
	string = string.lower()
	count = 0
	for i in string:
		if string.count(i) > 1:
			count += 1
	return True if count == 0 else False

print(is_isogram("booba"))
print(is_isogram("qwerty"))
print(is_isogram("blackbro"))
print(is_isogram("b"))
print(is_isogram("BoOb"))

'''
This was the top solution lol, i wish to think like this some day
def is_isogram(string):
    return len(string) == len(set(string.lower()))
'''