import math
# a=int(input("enter a number: "))
# print(f"factor of {a} are:",end=" ")
# for i in range(1,a+1):
#     if(a%i==0):
#         print(i,end=" ")

a=int(input("enter a number: "))
print(f"factor of {a} are:",end=" ")
l=[]
for i in range(1,int(math.sqrt(a))+1):
    if(a%i==0):
        l.append(i)
        if(1!=a//i):
            l.append(a//i)
l=sorted(l)
print(*l)