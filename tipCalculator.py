print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
total_people = int(input("How many people to split the bill?"))
contri_per_person = ((total_bill * (tip/100)) + total_bill) / total_people
print(f"Each Person should pay: ${contri_per_person}")