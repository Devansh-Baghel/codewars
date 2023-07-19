# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e
'''
Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

'''
def first_non_repeating_letter(s):
    res = ""
    s_upper = s[::-1].upper()
    s = s[::-1]
    for i in range(len(s_upper)):
        if s_upper.count(s_upper[i]) == 1:
            res = s[i]
                
    return res
