#exercise8

# The list is initialized with specific names 
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# first Step : Search  the name "Sam" in the list
search_name = "Sam"

if search_name in names:
    print(f"{search_name} is found in the list.")
else:
    print(f"{search_name} is not found in the list.")

# Step two : Implement the search functionality based on user input.
user_input = input("\nEnter a name to search for: ")

if user_input in names:
    print(f"{user_input} is found in the list.")
else:
    print(f"{user_input} is not found in the list.")
