n = int(input("Enter a Palindrome"))
m = n
res = 0
while m>0:
        i = m%10
        res = res*10+i
        m = m/10
        print(res)

if res==n:
    print("is a palindrome")
else:
    print("not a palindrome"