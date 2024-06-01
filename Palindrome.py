a=int(input("Enter a number to check palindrome or not: "))
temp=str(a)
temp=temp[::-1]
temp=int(temp)
if(temp==a):
    print(f"{a} is plaindrome number")
else:
    print(f"{a} is not a palindrome number")
