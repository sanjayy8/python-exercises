# Question 1:
#take two numbers from user perform arithmetic operations

a=int(input("Enter the value for a:"))
b=int(input("Enter the value for b:"))
print("Add:",a+b)
print("Sub:",a-b)
print("Mul:",a*b)
print("Div:",a/b)
print("Mod:",a%b)
print("Floor Div:",a//b)
print("Exp:",a**b)


#Question 2
#Calculating Area & Perimeter for Rectangle,square & circle

length=int(input("Enter the length:"))
breadth=int(input("Enter the breadth:"))
print("Area of rectangle:",length*breadth)
print("Perimeter of rectangle:",2*(length*breadth))
radius=float(input("Enter the radius:"))
print("Radius of circle:",3.14*(radius**2))
print("Perimeter of circle:",2*3.14*radius)
side=int(input("Enter the side:"))
print("Area of square:",side*side)
print("Perimeter of square:",4*side)


# Question 3:
#Average of three numbers

num1=int(input("Number 1:")) 
num2=int(input("Number 2:"))
num3=int(input("Number 3:"))
Avg=(num1+num2+num3)/3
print("Average:",Avg)


#Question 4:
#perform two numbers is equal,greater than,less then or equal to

a=10
b=5
print(a==b)
print(a>b or b>a)
print(a<=b)


#Question 5:
#Square root of a number

a=float(input("Enter a number:"))
print("Square root of a number:",sqrt(a))


#Question 6:
#Simple interest & Compound interest

p=float(input("Enter the principle amount:"))
r=float(input("Enter the rate of interest:"))
t=float(input("Enter the time:"))
SI=p*r*t/100
print("Simple interest:",SI)
amount=p*(1+r/100)**t
CI=amount-p
print("Compound Interest:",CI)


#Question 7:

x=10
x+=5
print("Add:",x)
x-=3
print("Sub:",x)
x*=2
print("Mul:",x)
x/=4
print("Div:",x)
x%=2
print("Mod:",x)
x**=3
print("Exp:",x)


#Question 8:
#Swapping of 2 numbers using arithmetic operators

num1=float(input("Enter number 1:"))
num2=float(input("Enter number 2:"))



#Question 9:
#using and / or

name=str(input("Enter the name:"))
password=int(input("Enter the password:"))
if name=='sanjay' and password==123:
    print("Valid")
    if name=='sanjay' or password==123:
        print("Valid")

    else:
        print("Not valid")

else:
    print("Not valid")
