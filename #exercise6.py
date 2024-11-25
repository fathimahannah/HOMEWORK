#exercise6


# Step 1: Set the correct password
correct_password = "12345"

# Step 2: Keep asking for the password until it's entered correctly
while True:
    # Ask the user to type the password
    entered_password = input("Please enter the password: ")

    # Step 3: Check if the typed password is correct
    if entered_password == correct_password:
        print("right password.you're in.")
        break  # Stop asking for the password once the correct one is entered
    else:
        print("Incorrect password. Please try again.")  # If the password is wrong, ask again


