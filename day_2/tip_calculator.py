print("Welcome to the tip calculator!")

bill = int(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

to_pay = bill / people * (tip / 100 + 1)
print(f"Each person should pay: ${to_pay:.2f}")