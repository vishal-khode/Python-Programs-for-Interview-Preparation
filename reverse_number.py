a=int(input("enter a number to be reversed: "))
n=a
rev=0
while(a!=0):
    rem=a%10
    rev=rev*10+rem
    a//=10
print(f"The reverse of {n} is:",rev)