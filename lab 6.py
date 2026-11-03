
#   MAP() AND FILTER()

#   EASY

# MAP()

# 1. Double every number in a list.
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))
print("Double:", result)


# 2. Find the square of every number.
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, numbers))
print("Squares:", result)


# 3. Add 5 to every number.
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x + 5, numbers))
print("Add 5:", result)


# 4. Multiply every number by 10.
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 10, numbers))
print("Multiply by 10:", result)


# 5. Convert all names to uppercase.
names = ["ram", "ravi", "kumar"]
result = list(map(lambda x: x.upper(), names))
print("Uppercase names:", result)


# FILTER()

# 6. Get all even numbers.
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", result)


# 7. Get all odd numbers.
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers:", result)


# 8. Get numbers greater than 10.
numbers = [5, 10, 15, 20, 25]
result = list(filter(lambda x: x > 10, numbers))
print("Greater than 10:", result)


# 9. Get numbers less than 50.
numbers = [10, 25, 50, 60, 75]
result = list(filter(lambda x: x < 50, numbers))
print("Less than 50:", result)


# 10. Get numbers divisible by 5.
numbers = [10, 12, 15, 20, 23, 25]
result = list(filter(lambda x: x % 5 == 0, numbers))
print("Divisible by 5:", result)


# MODERATE


# MAP()

# 11. Find the cube of every number.
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 3, numbers))
print("Cubes:", result)


# 12. Find the length of every word in a list.
words = ["apple", "banana", "cat", "orange"]
result = list(map(lambda x: len(x), words))
print("Word lengths:", result)


# 13. Convert temperatures from Celsius to Fahrenheit.
celsius = [0, 10, 20, 30, 40]
result = list(map(lambda x: (x * 9/5) + 32, celsius))
print("Fahrenheit:", result)


# 14. Add 10% to every price in a list.
prices = [100, 200, 300, 400]
result = list(map(lambda x: x * 1.10, prices))
print("Prices after 10% increase:", result)


# 15. Convert a list of names into their first-letter uppercase format.
names = ["sanjay", "ravi", "kumar"]
result = list(map(lambda x: x.capitalize(), names))
print("Capitalized names:", result)


# FILTER()

# 16. Get numbers between 10 and 50.
numbers = [5, 10, 20, 30, 50, 60]
result = list(filter(lambda x: 10 <= x <= 50, numbers))
print("Between 10 and 50:", result)


# 17. Get numbers divisible by both 2 and 3.
numbers = [6, 8, 12, 15, 18, 20]
result = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers))
print("Divisible by both 2 and 3:", result)


# 18. Get names starting with "A".
names = ["Arun", "Ravi", "Anu", "Kumar"]
result = list(filter(lambda x: x.startswith("A"), names))
print("Names starting with A:", result)


# 19. Get words having more than 5 characters.
words = ["apple", "banana", "cat", "orange"]
result = list(filter(lambda x: len(x) > 5, words))
print("Words with more than 5 characters:", result)


# 20. Get positive numbers from a list.
numbers = [-5, 10, -2, 20, 0, 15]
result = list(filter(lambda x: x > 0, numbers))
print("Positive numbers:", result)


# COMBINED MODERATE


# 21. Filter even numbers and find their squares.
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
result = list(map(lambda x: x ** 2, even))
print("Squares of even numbers:", result)


# 22. Filter numbers greater than 10 and double them.
numbers = [5, 10, 15, 20, 25]
greater = list(filter(lambda x: x > 10, numbers))
result = list(map(lambda x: x * 2, greater))
print("Double of numbers greater than 10:", result)


# 23. Filter names starting with "A" and convert them to uppercase.
names = ["Arun", "Ravi", "Anu", "Kumar"]
filtered = list(filter(lambda x: x.startswith("A"), names))
result = list(map(lambda x: x.upper(), filtered))
print("Uppercase names starting with A:", result)


# 24. Filter odd numbers and find their cubes.
numbers = [1, 2, 3, 4, 5, 6]
odd = list(filter(lambda x: x % 2 != 0, numbers))
result = list(map(lambda x: x ** 3, odd))
print("Cubes of odd numbers:", result)


# 25. Filter words with more than 4 characters and find their lengths.
words = ["apple", "cat", "banana", "dog", "orange"]
filtered = list(filter(lambda x: len(x) > 4, words))
result = list(map(lambda x: len(x), filtered))
print("Lengths of words:", result)
