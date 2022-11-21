# Greeting for the calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip = 1 + (percent/100)
people = int(input("How many people to split the bill? "))



total = (bill*tip)/people
# Also couldve written as total = "{:.2f}".format(total) and just reference as {total}
# Instead of using round(num,2) we can use format to create {num:.2f} for 2 decimal places
print(f"Each person should pay: ${total:.2f}")