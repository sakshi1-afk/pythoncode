a = float(input("enter first number:"))
b = float(input("enter second number:"))
c = float(input("enter third number:"))
if (a>=b and a>=c):
    print("greatest number is:", a)
elif (b>=a and b>=c):
    print("greatest number is:",b)
else:
    print("greatest number is:",c)
# This program finds the greatest of three numbers entered by the user.