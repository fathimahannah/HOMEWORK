#exercise4

#list of f European countries and their capitals

# Dictionary of countries and their capitals
countries_and_capitals = {
    "France": "Paris",
    "albania": "tirana",
    "greece": "athens",
    "ireland": "dublin",
    "United Kingdom": "London",
    "iceland": "reykjavik",
    "monaco": "monaco",
    "Sweden": "Stockholm",
    "Austria": "Vienna",
    "kosovo": "pristina"
}

# Loop through each country and its corresponding capital
for country, correct_capital in countries_and_capitals.items():
    # Ask the user for the capital of the current country
    user_answer = input(f"Can you guess the capital of {country}? ").strip()

    # Check if the entered answer is correct, without considering case sensitivity
    if user_answer.lower() == correct_capital.lower():
        print(f"Yes, {correct_capital} is the correct capital of {country}! Well done!\n")
    else:
        print(f"Oops! The correct capital of {country} is {correct_capital}.\n")

        
