a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
c=int(input("Enter a third number: "))

if(a>b and a>c):
    print(f"{a} is largest among the three numbers.")
elif(b>a and b>c):
    print(f"{b} is largest among the three numbers.")
elif(c>a and c>b):
    print(f"{c} is largest among the three numbers.")
else:
    print(f"{a} {b} {c} are the same numbers.")
