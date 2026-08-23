#Question 1:

for i in range (1,11):
    print(i,end=' ')


#Question 2:

for i in range(10,0,-1):
    print(i,end=' ')


#Question 3:

for i in range(1,51):
    if i%2==0:
        print(i,end=' ')

#Question 4:

for i in range(1,51):
    if i%2!=0:
        print(i,end=' ')


#Question 5:

for i in range(1,11):
    print('5','*',i,'=',i*5)


#Question 6:

a=0
for i in range(1,101):
    a=a+i
print(a)


#Question 7:

for i in range(1,11):
    print(i**2,end=' ')


#Question 8:

for i in 'PYTHON':
    print(i,end=' ')


#Question 9:

count = 0
s = input("Enter a string: ")
for i in s:
    if i in "aeiouAEIOU":
        count += 1
print("Number of vowels:", count)


#Question 10:

a=0
for i in range(1,101):
    if i%2==0:
        a=a+i   
print(a)


#Question 11:

f=1
a=int(input("Enter the value:"))
for i in range(1,a+1):
    f*=i
print(f)


#Question 12:

count=0
n=int(input("Enter the number:"))
for i in range(1,n+1):
    if n%i==0:
        count=count+1

if count==2:
    print("Prime")
else:
    print("Not prime")


#Question 13:

for n in range(1, 101):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(n,end=' ')


#Question 14:

numbers = [10, 45, 23, 89, 12, 67]
largest = 0
for i in numbers:
    if i > largest:
        largest = i
print("Largest Number:",largest)

#Question 15:

numbers = [10, -5, 20, -8, 15, -2]
positive = 0
negative = 0
for i in numbers:
    if i > 0:
        positive += 1
    else:
        negative += 1
print("Positive:", positive)
print("Negative:", negative)


#Question 16:

text ='PYTHON'
reverse = ""
for i in text:
    reverse = i + reverse
print(reverse)


#Question 17:

count = 0
text = input("Enter a string: ")
char = input("Enter a character: ")
for i in text:
    if i == char:
        count += 1
print(count)
























    
