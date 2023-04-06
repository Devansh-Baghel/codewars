# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

'''
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false


'''

def xo(s):
	s = s.lower()
	return True if s.count("x") == s.count("o") else False

print(xo("xxoo"))
print(xo("xxo1o"))
print(xo("xxo"))
print(xo("xxoxo0oxo"))