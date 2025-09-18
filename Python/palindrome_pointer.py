word = input("Enter a palindrome ")

list1 = list(word)
print(list1)

length = len(word)
isPalindrome = False

k = 0
j = length-1

while k<j:
    if char_k==char_j:
        isPalindrome = True
    else:
        isPalindrome= False
        break;
k+=1
j+=1

