# Program to display the multiplication table of a given number
# Skip the multiplication by 5 using 'continue' statement

n= int(input("Enter a number to display its multiplication table: "))

for i in range (1, 11):
    if i==5:
        continue
    else:
        print(n,"x",i,"=",n*i)
