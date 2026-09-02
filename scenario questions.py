1#atm withrawal

balance=10000
amount=12000
if amount<=balance:
    print("withrawal successful")
else:
    print("not withrawal")


2#login system

username=str(input("enter username:"))
password=str(input("enter password:"))
if username=="Sanjay":
    if password=="2006":
        print("login successful")
    else:
        print("worng password")
else:
    print("worng username")


3#oline shopping discount

amount=int(input("enter amount:"))
if amount>500:
    print("20% discount")
else:
    print("not discount")

4#student result system

mark=int(input("mark:"))
if mark >= 90:
    print("A")
elif mark >= 75:
    print("B")
elif mark >= 60:
    print("C")
else:
    print("Fail")

5#password attempts

correct_password = "Sanjay@2006"

for attempt in range(3):
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful")
        break
    else:
        print("Wrong password")

6#atm menu

while True:
    print("\n1. Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance")
    elif choice == 2:
        print("Withdraw")
    elif choice == 3:
        print("Deposit")
    elif choice == 4:
        print("Thank you")
        break
    else:
        print("Invalid choice")


 
7# Shopping

products = ["Laptop", "Mobile", "Out of Stock", "Mouse"]
for product in products:
    if product == "Out of Stock":
        continue

    print(product)

8# Parking System

vehicles = ["TN01AB1234", "TN22CD5678", "TN30EF9999"]

for vehicle in vehicles:
    if vehicle == "TN30EF9999":
        print("Vehicle found")
        break

9#Email Validation

emails = [
    "abc@gmail.com",
    "hello@gmail.com",
    "invalidemail",
    "test@yahoo.com"
]

for email in emails:
    if "@"  not in email:
        continue

    print("Valid:", email)


10#Number Searching

for i in range(1, 101):
    if i == 75:
        print("Number found")
        break

11# Bank Loan Eligibility

age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))

if age >= 21:
    if salary >= 30000:
        print("Loan approved")
    else:
        print("Salary is too low")
else:
    print("Age requirement not met")


12#College Admission

mark = int(input("Enter your mark: "))
documents = input("Have you submitted the documents? (yes/no): ")

if mark >= 60:
    if documents == "yes":
        print("Admission approved")
    else:
        print("Submit documents")
else:
    print("Not eligible")

13#Employee Attendance

attendance = ["Present", "Absent", "Present", "Present", "Absent"]

for status in attendance:
    if status == "Present":
        print("Employee is present")


14#Security Monitoring

while True:
    login = input("Enter login status: ")

    if login == "suspicious":
        print("Alert!")
        break

    print("Monitoring...")


15# Testing Multiple Inputs

inputs = [10, 20, -5, 30, 40]
n = int(input("Enter how many values: "))
for value in inputs:
    if value < 0:
        continue

    print("Testing:", value)


16#Incomplete Function

def payment():
    pass

17#Interview Scenario – Break or Continue

customer_ids = range(1, 1001)

for customer_id in customer_ids:
    if customer_id == 500:
        break

    print("Processing customer:", customer_id)


customer_ids = range(1, 1001)

for customer_id in customer_ids:
    if customer_id == 500:
        continue

    print("Processing customer:", customer_id)


18# Interview Scenario – For or While?

for i in range(100):
    name = input("Enter student name: ")
    print("Processing student:", name)


correct_password = "python123"

password = input("Enter your password: ")

while password != correct_password:
    print("Incorrect password. Try again.")
    password = input("Enter your password: ")

print("Login successful!")


19#Tricky Real-Time Scenario

menu = ["pizza", "burger", "pasta"]

while True:
    print("\nMenu:", menu)
    item = input("Enter your order (or 'exit' to stop): ")

    if item == "exit":
        break

    if item not in menu:
        print("Item unavailable. Skipping...")
        continue

    print("Order placed:", item)

print("Thank you for ordering!")
