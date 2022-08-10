# Greeting for the calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip = 1 + (percent/100)
people = int(input("How many people to split the bill? "))

total = round(((bill*tip)/people),2)

print(f"Each person should pay: ${total}")