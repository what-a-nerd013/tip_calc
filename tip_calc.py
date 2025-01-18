#my first python project, don't hate :)
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 20 25 30"))
people = int(input("How many people to split the bill? "))
each_person = (bill / 100 * tip + bill) / people
final_amount = round(each_person, 2)
print(f"Each person should pay: ${final_amount}")