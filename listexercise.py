#Creating a List
fruits = ["apple", "banana", "cherry", "grapes","watermelon"]
print(fruits)
#Accessing Elements
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print("First element:", colors[0])
print("Third element:", colors[2])
print("Last element:", colors[-1])
#Modifying a List
numbers=[10, 20, 30, 40, 50]
numbers[1]=25
numbers.append(60)
print(numbers)
#List Slicing
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = names[:3]
print(subset)
#Looping through a List
numbers = list(range(1, 11))
for number in numbers:
    print(number ** 2)
#List Methods: Append and Extend
shopping_cart = []
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs')
shopping_cart.extend(['butter', 'cheese'])
print(shopping_cart)
#Finding Maximum and Minimum in a List
numbers = [45, 22, 88, 56, 92, 33]
maximum_value = max(numbers)
minimum_value = min(numbers)
print("Maximum value:", maximum_value)
print("Minimum value:", minimum_value)
#Counting Occurrences
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
count_a = letters.count('a')
print("The letter 'a' appears", count_a, "times.")
#List Comprehension
squares_of_evens = [x**2 for x in range(11) if x % 2 == 0]
print(squares_of_evens)
#Removing Duplicates
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_nums = list(set(nums))
print(unique_nums)