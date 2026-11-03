
# PYTHON EXCEPTION HANDLING AND FILE HANDLING


# 1. EXCEPTIONAL HANDLING
try:
    a = int(input("Enter the number: "))
    print("Number:", a)
except ValueError:
    print("Not a number")


# 2. ZERODIVISIONERROR
try:
    x = 10 / 0
    print("Divisible")
except ZeroDivisionError:
    print("Cannot divide by zero")


# 3. TRY, EXCEPT AND ELSE
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    x = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Value error: Enter numbers only")
else:
    print("Result:", x)
    print("Okkk")


# 4. TYPEERROR
try:
    a = "Hii" + 5
except TypeError:
    print("Cannot add string and integer")


# 5. RAISE
age = int(input("Enter age: "))
if age < 18:
    raise ValueError("Cannot register")
else:
    print("Registered")


# 6. INDEX ERROR
try:
    a = [1, 2, 3, 4, 5]
    print(a[10])
except IndexError:
    print("No index position")


# 7. KEY ERROR
try:
    a = {"Name": "Joy", "Course": "Python"}
    print(a["Age"])
except KeyError:
    print("Key not found")


# FILE HANDLING


# 8. CREATE AND WRITE FILE
f = open("Python.txt", "w")
f.write("Hii this is Python")
f.close()
print("Successful")


# 9. READ THE FILE
f = open("Python.txt", "r")
a = f.read()
print(a)
f.close()


# 10. APPEND AND READ
f = open("Python.txt", "a")
f.write("\nJoy didnt attend the class")
f.close()
print("Successful")
f = open("Python.txt", "r")
a = f.read()
print(a)
f.close()


# 11. LINE BY LINE USING FOR LOOP
f = open("Student.txt", "w")
f.write("Student 1\nStudent 2\nStudent 3")
f.close()

f = open("Student.txt", "r")
for line in f:
    print(line.strip())
f.close()


# 12. FILE HANDLING USING WITH
with open("Student.txt", "w") as f:
    f.write("Hello")
with open("Student.txt", "r") as f:
    print(f.read())


# 13. COUNT THE LETTERS IN THE FILE
with open("Student.txt", "r") as f:
    a = f.read()
    b = a.strip()
print("Total:", len(b))


# 14. FILE HANDLING WITH EXCEPTION HANDLING
try:
    with open("Stunt.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")


# 15. REMOVE FILE USING OS
import os
if os.path.exists("Student.txt"):
    os.remove("Student.txt")
    print("Removed")
else:
    print("File not found")
