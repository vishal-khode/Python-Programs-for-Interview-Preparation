import math
def primenumber(a,b):
    l=[]
    if a<2:
        a=2
        l.append(a)
    for i in range(a,b+1):
        flag=False
        for k in range(2,(int(math.sqrt(i))+1)):
            if(i%k==0):
                flag=True
                break
        if(flag==False):
            l.append(i)
    return l

a=int(input("Enter a number: "))
b=int(input("Enter a number "))
print(f"The Prime number between the range {a} and {b} are ",end="")
a=primenumber(a,b)
print(*a)