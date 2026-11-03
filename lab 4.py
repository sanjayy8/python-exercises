# 1. Write a Python program to take your name as input and print it.

name = input("Enter your name: ")
print("My name is", name)


# 2. Write a program to find the length of a string.

str1 = input("Enter a string: ")
print("Length of string:", len(str1))


# 3. Write a program to convert a string into uppercase.

str1 = input("Enter a string: ")
print("Uppercase:", str1.upper())


# 4. Write a program to convert a string into lowercase.

str1 = input("Enter a string: ")
print("Lowercase:", str1.lower())

# 5. Write a program to print the first and last character of a string.

str1 = input("Enter a string: ")
print("First character:", str1[0])
print("Last character:", str1[-1])


# 6. Write a program to check whether a string starts with "A" using startswith().

str1 = input("Enter a string: ")
if str1.startswith("A"):
    print("String starts with A")
else:
    print("String does not start with A")


# 7. Write a program to check whether a string ends with "ing" using endswith().

str1 = input("Enter a string: ")

if str1.endswith("ing"):
    print("String ends with ing")
else:
    print("String does not end with ing")


# 8. Write a program to check whether the given string contains only numbers using isdigit().

str1 = input("Enter a string: ")
if str1.isdigit():
    print("Contains only numbers")
else:
    print("Does not contain only numbers")


# 9. Write a program to check whether the given string contains only alphabets using isalpha().

str1 = input("Enter a string: ")
if str1.isalpha():
    print("Contains only alphabets")
else:
    print("Does not contain only alphabets")



# 10. Write a program to count a particular character in a string using count().

str1 = input("Enter a string: ")
ch = input("Enter a character: ")
print("Count:", str1.count(ch))



# 11. Write a program to find the position of a character using find().

str1 = input("Enter a string: ")
ch = input("Enter a character: ")
print("Position:", str1.find(ch))



# 12. Write a program to replace a word in a string using replace().

str1 = input("Enter a sentence: ")
old = input("Enter word to replace: ")
new = input("Enter new word: ")
print("New string:", str1.replace(old, new))


# 13. Write a program to remove extra spaces from a string using strip().

str1 = input("Enter a string: ")
print("After removing spaces:", str1.strip())



# 14. Write a program to split a sentence into words using split().

str1 = input("Enter a sentence: ")
words = str1.split()
print("Words:", words)




# 15. Write a program to reverse a string using slicing.

str1 = input("Enter a string: ")
print("Reversed string:", str1[::-1])




# 16. Write a program to print the first 3 characters using slicing.

str1 = input("Enter a string: ")
print("First 3 characters:", str1[:3])



# 17. Write a program to print the last 3 characters using slicing.

str1 = input("Enter a string: ")
print("Last 3 characters:", str1[-3:])




# 18. Write a program to print characters from index 2 to 5 using slicing.

str1 = input("Enter a string: ")
print("Characters:", str1[2:6])



# 19. Write a program to print alternate characters using slicing.

str1 = input("Enter a string: ")
print("Alternate characters:", str1[::2])


# 20. Write a program using format() to display a person's name, age, and city in a sentence.

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
print("My name is {}, I am {} years old and I live in {}.".format(name, age, city))
