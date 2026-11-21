# List exercise
# sum, largest, smallest and average of a list of numbers
print("\nList exercise")
numbers = [4,8,15,16,23,42]
sum_of_numbers = sum(numbers)
largest_number = max(numbers)
smallest_number = min(numbers)
average_of_numbers = sum_of_numbers / len(numbers)
numbers.append(99)

# Print
print("Sum of numbers:", sum_of_numbers)
print("Largest number:", largest_number)
print("Smallest number:", smallest_number)
print("Average of numbers:", average_of_numbers, "\n" )
print("List after adding a number:", numbers, "\n")

# remove
numbers.remove(15)
print("List after removing a number:", numbers, "\n")


# Tuple exercise
# Tuple holding person's name, age and city
print("\nTuple exercise")
person = ("John Doe", 30, "New York")
for item in person:
    print(f"{item}")

# Dictionary exercise
print("\nDictionary exercise")
text = "the cat and the dog and the bird"

textSplit = text.split()

count={}


for word in textSplit:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1

for word, times in count.items():
    print(f"the word '{word}' appears {times} times in the text.")


# Dictionary loockup
print("\nDictionary exercise")
fruits_prices = {
    "apple": 0.5,
    "banana": 0.3,
    "orange": 0.7,
    "grape": 1.2
}

fruit = input("Enter a fruit name: ")
if fruit in fruits_prices:
    price = fruits_prices[fruit]
    print(f"The price of the fruit is: ${price} \n")
else:
    print("Fruit not found! \n")

# Set operations
print("\nSet operations")
a = {1,2,3,4,5}
b = {4,5,6,7,8}
union = a.union(b)
intersection = a.intersection(b)
elements_a_not_b = a.difference(b)
symetric_difference = a.symmetric_difference(b)
print("Union:", union)
print("Intersection:", intersection)
print("Elements in A but not in B:", elements_a_not_b)
print("Symmetric difference:", symetric_difference, "\n")


# Combined exercise
print("\nCombined exercise")
students = [
    {"firstName": "Javier", "lastName": "Gonzalez", "age": 15, "grades": [8,9,10]},
    {"firstName": "María", "lastName": "López", "age": 16, "grades": [7,8,9]},
    {"firstName": "Carlos", "lastName": "Rodríguez", "age": 14, "grades": [9,10,10]}
]

full_name = f"Name: {students[0]['firstName']} {students[0]['lastName']}"
print(full_name, "\n")

best_name = ""
best_avg_grade = 0
for student in students:
    full_name = f"Name: {student['firstName']} {student['lastName']}"
    print(full_name, "Grades:", student['grades'])
    average_grade = sum(student['grades']) / len(student['grades'])
    if average_grade > best_avg_grade:
        best_avg_grade = average_grade
        best_name = full_name

print(f"Highest average grade: {best_name}, {best_avg_grade:.2f}", "\n")