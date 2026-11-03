#exceptional handling
try:
     a=int(input("Enter the number:"))
     print("Number:",a)
except:
    print("Not a number")



#Zerodivisionerror

try:
    x=10/0
    print("Divisible")
except ZeroDivisionError:
    print("Not a number")
