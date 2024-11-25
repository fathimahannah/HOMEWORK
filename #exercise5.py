#exercise5

# Step 1: Create a list for month number and number of days
days_in_month = {
    1: 31,   # January
    2: 28,   # February (non-leap year by default)
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

# Step 2: Input handling to get the month number
month = int(input("Enter the month number (1-12): "))

# Step 3: Check if the input is valid
if 1 <= month <= 12:
    # If the month is February, check for leap year
    if month == 2:
        # Ask if it's a leap year
        year = int(input("Enter the year to check if it's a leap year: "))
        
        # Leap year check: A year is a leap year if it's divisible by 4, but not by 100 unless also divisible by 400
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"February has 29 days in {year}.")
        else:
            print(f"February has 28 days in {year}.")
    else:
        # For other months, just print the number of days from the dictionary
        print(f"Month {month} has {days_in_month[month]} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
