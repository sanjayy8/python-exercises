#Python Tasks – for Loop with break, continue, pass


#BREAK


#1. Using a for loop, print numbers from 1 to 10 and stop when the number is 5.

for i in range(1, 11):
    print(i)
    if i == 5:
        break


#2.Using a for loop, print numbers from 1 to 20 and stop when the number is 10.

    for i in range(1, 21):
      print(i)
      if i == 10:
        break


#3. Using a for loop, print the numbers 1 to 10 and stop when the number is divisible by 4.


for i in range(1, 11):
    print(i)
    if i % 4 == 0:
        break



#4. Using a for loop, search for the number 7 in a list and stop when it is found.

numbers = [2, 4, 6, 7, 9, 10]
for i in numbers:
    print(i)
    if i == 7:
        print("7 found")
        break




#CONTINUE



#5. Using a for loop, print numbers from 1 to 10, skipping 5.


for i in range(1, 11):
    if i == 5:
        continue
    print(i)



#6. Using a for loop, print numbers from 1 to 20, skipping even numbers.



for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)




#7. Using a for loop, print numbers from 1 to 15, skipping numbers divisible by 3.


    for i in range(1, 16):
      if i % 3 == 0:
        continue
    print(i)



#8. Using a for loop, print all characters in "PYTHON" except "O".


word = "PYTHON"

for ch in word:
    if ch == "O":
        continue
    print(ch)



#PASS




#9. Using a for loop, print numbers from 1 to 10 and use pass when the number is 5.


for i in range(1, 11):
    if i == 5:
        pass
    print(i)



#10. Using a for loop, print the names in a list and use pass when the name is "Ravi".


names = ["Arun", "Ravi", "Kumar", "Sanjay"]
for name in names:
    if name == "Ravi":
        pass
    print(name)

#11. Using a for loop, check numbers from 1 to 10 and use pass for even numbers.

for i in range(1, 11):
    if i % 2 == 0:
        pass
    print(i)



#12. Write a for loop from 1 to 5 and use pass inside the loop.

    for i in range(1, 6):
     pass


#MIXED PRACTICE


#13. Print numbers from 1 to 20 using a for loop. Skip even numbers and stop at 15.


for i in range(1, 11):
    if i % 2 == 0:
        pass
    print(i)


#14. Print numbers from 1 to 10. Use pass for 5 and continue for 7.

for i in range(1, 11):
    if i == 5:
        pass
    if i == 7:
        continue
    print(i)




#15. Print numbers from 1 to 20. Skip multiples of 3 and stop when the number reaches 18.


    for i in range(1, 21):
     if i == 18:
        break
    if i % 3 == 0:
        continue
    print(i)
