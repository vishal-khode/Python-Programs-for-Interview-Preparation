a=int(input("enter a number to check armstrong: "))
n=a
sizeofnumber=len(str(a))
ans=0
while a!=0:
    i=a%10
    ans+=(i**sizeofnumber)
    a//=10
if(ans==n):
    print(f"Yes {n} is ArmStrong number")
else:
    print(f"No {n} is not ArmStrong number")