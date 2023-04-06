# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python

'''
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 12+22+22=91^2 + 2^2 + 2^2 = 912+22+22=9.

'''

def square_sum(numbers):
    result = []
    for i in numbers:
        i = i*i
        result.append(i)
    return sum(result)
print(square_sum([3,2,3,4]))