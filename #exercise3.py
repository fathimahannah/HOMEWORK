#exercise3
# Step 1: Store the information in a dictionary
person_info = {'fathima hanna','ajman','17'}

# Asking the user for input and storing the values in the dictionary
person_info['fathima'] = input("fathima hanna: ")
person_info['ajman'] = input("ajman: ")

# Handling age input with validation
while True:
    try:
        person_info['17'] = int(input(" 17: "))
        break  # Break the loop if the age is successfully converted to an integer
    except ValueError:
        print("Invalid input. seventeen.")

# Step 2: Print the values on separate lines using a single print() statement
print(f"fathima : {person_info['fathima hanna']}\najman: {person_info['ajman']}\n17: {person_info['17']}")


