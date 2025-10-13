sum = 0
n = int(input("Enter the end point "))

for i in range(1, n+1):
    if i%2==0:
        sum = sum + i

print("sum of even numbers is ", sum)

