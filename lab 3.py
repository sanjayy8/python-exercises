
#forloop
#1.print numbers from 1 to 10

for i in range (1,11):
    print(i)


#2.print numbers from 10 to 1

for i in range(10,0,-1):
    print(i)
    


#3.print all even numbers from 1 to 20

for i in range(1,21):
    if i%2==0:
        print("even:",i)
 

#4.print all odd numbers from 1 to 20

for i in range(0,20):
    if i%2!=0:
        print("odd:",i)


#5.print a multiplication table of number

for i in range(1,21):
    print('5','*',i,'=',5*i)


#6.find the sum of numbers from 1 to 100

sum=0
for i in range(1,101):
    sum=sum+i
print(sum)
    

#7.find the sum of even numbers from 1 tom 50

sum=0
for i in range(1,51):
    if i%2==0:
        sum=sum+i
print(sum)
   

#8.print each character of a string

s='PYTHON'
for i in s:
    print(i)



#9.count the number of characters in the string without using len
a='SANAJY'
count=0
for i in a:
    count+=1
print(count)

#10.print the squares of number from 1 to 10

for i in range(1,11):
    print(i**2)

