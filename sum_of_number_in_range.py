a=int(input("Enter a first number"))
b=int(input("Enter a second number"))
tot=0
for i in range(a,b+1):
    tot+=i
print(f"The sum of the number given in a range: ",end="")
print(tot)
