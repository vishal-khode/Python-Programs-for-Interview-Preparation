# def fib(n):
#     if(n<=1):
#         return 1
#     return fib(n-1)+fib(n-2)
# a=int(input("Enter a number to print fibnaocii series: "))
# for i in range(a):
#     print(fib(i),end=" ")
#Recursive Method


#Iterative method
a=int(input("enter a number"))
n1,n2=0,1
for i in range(2,a):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")