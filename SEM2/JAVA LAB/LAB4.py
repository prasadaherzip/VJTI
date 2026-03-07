from functools import reduce

numbers = [2, 5, 8, 11, 14, 17, 20]

even = list(filter(lambda n: n%2 == 0, numbers))
print("Even Numbers", even)

sqrd = list(map(lambda n: n*n, numbers))
print("Squared Numbers:", sqrd)

sum = reduce(lambda a,b: a+b, numbers)
print("Sum of Numbers:", sum)

result = reduce(lambda a,b: a+b,
                map(lambda n: n*n,
                    filter(lambda n: n%2 == 0, numbers)),
                    0)

print("Sum of squares of even numbers:", result)

