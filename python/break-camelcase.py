# https://www.codewars.com/kata/5208f99aee097e6552000148

'''
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
'''

def solution(s):
    break_point = 0

    for i in s:
        if i == i.upper():
            break_point = s.index(i)

    return s[0:break_point] + " " + s[break_point:]


# This currently works with camels with only one hump
# Works with camelCase
# Not with camelCaseCase

# Will make it work later


print(solution("asdasfA"))