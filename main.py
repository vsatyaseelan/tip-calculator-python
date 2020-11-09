print("Welcome to the Tip Calculator")
total = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 20, or 15? "))
people = int(input("How many people to split the bill? "))
tip_amount = total * (percentage / 100)
pay = round((total + tip_amount) / people, 2)
message = f"Each person should pay: ${pay}"
print(message)