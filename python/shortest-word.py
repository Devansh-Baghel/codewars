# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.


'''

def find_short(s):
    a = s.split()
    d = len(a[0])
    for i in a:
        if len(i) < d:
            d = len(i)

    return d

print(find_short("as sd afa we faesf a a f f fsv"))