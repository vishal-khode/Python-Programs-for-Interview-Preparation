a=int(input("Enter a Year: "))
if(a%4==0 and a%100!=0):
    print(f"{a} is a leap year")
elif(a%400==0):
    print(f"{a} is leap year")
else:
    print(f"{a} is not a leap year")
    