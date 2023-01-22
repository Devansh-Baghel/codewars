def even_or_odd(number):
    if number%2 == 0:
        return "Even"
    elif number%2 == 1:
        return "Odd"

print(even_or_odd(1))
print(even_or_odd(2))
print(even_or_odd(5))
print(even_or_odd(100))
print(even_or_odd(-32))
print(even_or_odd(0))
print(even_or_odd("asf"))
