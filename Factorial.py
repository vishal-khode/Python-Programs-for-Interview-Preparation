def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)
a=int(input("Enter a number to find factorial: "))
print(f"factorial of {a} is",fact(a))