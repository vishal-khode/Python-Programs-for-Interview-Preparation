a=int(input("enter a number: "))
n=a
tot=0
while(a!=0):
    rem=a%10
    tot+=rem
    a//=10
print(f"the sum of the digits in a {n} is: ",end="")
print(tot)