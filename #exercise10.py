#exercise10

# Function to determine if a number is even or odd
def is_even_or_odd(num):

    # Check if the number is divisible by 2
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# the Main function 
def main():
    # Prompt the user to enter a number
    user_input = input("Enter a number to check if it is even or odd: ")
    
    try:
        # Try converting the input to an integer
        number = int(user_input)
        
        # Pass the number to the function
        result = is_even_or_odd(number)
        
        # Display the result to the user
        print(f"The number {number} is {result}.")
    
    except ValueError:
        # Handle the case where input is not a valid number
        print("That's not a valid number! Please enter an integer.")

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()

