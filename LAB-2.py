#if else

1.Odd or even

a=float(input("Enter the number:"))
if (a%2==0):
    print("The number is even")
else :
    print("The number is odd")
    

2.Eligible to vote

a=int(input("Enter your Age:"))
if a>=18:
    print("The person is Elegible to vote")
else:
    print("The person is not Eligible to vote")

3.Student pass or fail

marks=int(input("Enter your marks:"))
if (marks>=40):
    print("The student pass")
else:
        print("The Student Fail")

4.positive or negative

num=int(input("Enter the number:"))
if num>=0:
    print("The number is positve")
else:
    print("The number is negative")

# Elif

5.Assign grades based on marks

mark=int(input("Enter your Mark:"))
if (mark>=90):
    print("grade A")
elif 75<=mark<=89:
    print("grade B")
elif 50<=mark<=74:
    print("grade C")
else:
    print("Fail")

6.largest among three numbers

num1=float(input("Enter number 1:"))
num2=float(input("Enter number 2:"))
num3=float(input("Enter number 3:"))
if num1>num2 and num1>num3:
    print("number 1 is Largest:",num1)
elif num2>num1 and num2>num3:
    print("number 2 is Largest:",num2)
elif num3>num1 and num3>num2:
    print("number 3 is Largest:",num3)
else:
    print("Zero")

7.takes a number (1-7) prints in corresponding week

num=int(input("Enter the number:"))
if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thursday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("Not valid")

8. Simple Calculator

a=float(input("Enter a number1:"))
b=float(input("Enter a number2:"))
op=input("Enter operator:")
if op=='+':
    print("Addition:",a+b)
elif op=='-':
    print("Subtraction:",a-b)
elif op=='*':
    print("Multiplication:",a*b)
elif op=='/':
    print("Division:",a/b)
else:
    print("Not valid")

#Nested if else

9.program to validate login

name=str(input("Enter a username:"))
password=int(input("Enter a password:"))
if name=='sharvesh':
    print("Username Valid")
    if password==1234:
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")
    
10.Traffic Signal System

color=str(input("Enter a color:"))
if color=='red':
    print("Stop")
else:    
    if color=='yellow':
        print("Get Ready")
    else:
        if color=='green':
            print("Go")
        else:
             print("Not valid")
    
