
#1.USER DEFINED FUNCTIONS

'''
#question 1

def func():
    print("Hello World")
func()

'''
'''
#question 2

def func():
    print("SANJAY")
func()
'''
'''
#question 3

def func(a,b):
    print("Add:",a+b)
func(8,2)
'''
'''
#question 4


def func(a,b):
    print("Sub:",a-b)
func(8,2)
'''
'''
#question 5

def square(n):
    return n*n
number=int(input("Enter number:"))
print(square(number))
'''
'''
#question 6

def func(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")
n=int(input("Enter the number:"))
func(n)
'''
'''
#question 7

def func(n1,n2):
    if(n1>n2):
        print("largest number")
    else:
        print("smallest number")
n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
func(n1,n2)
'''
'''
#question 8

def rectangle_area(length,breadth):
    area = length*breadth
    return area
length=float(input("Enter length:"))
breadth=float(input("Enter breadth:"))
print("Area of rectangle:",rectangle_area(length,breadth))

'''
'''
#question 9

def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
n=int(input("Enter the number:"))
print(factorial(n))
'''
'''
#question 10

def func(a):
    if(a>0):
        print("Positive")
    elif(a<0):
        print("Negative")
    else:
        print("Zero")
a=int(input("Enter the number:"))
print(func(a))

'''


#2.RECURSIVE FUNCTIONS

'''
#question 11

def a(n):
    if n<=5:
        print(n)
        a(n+1)
a(1)

'''
'''
#question 12

def b(n):
    if n==0:
        return
    print(n)
    b(n-1)
b(5)
'''

#question 13


def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
n=int(input("Enter the number:"))
print(factorial(n))
