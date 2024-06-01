import math
a=int(input("enter a number: "))
flag=False
squareroot=int(math.sqrt(a))
for i in range(2,squareroot):
    if(a%i==0):
        print(f"{a} is not a Prime Number.")
        break
    else:
        flag=True
if(flag):
    print(f"{a} is a prime number")