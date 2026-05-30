print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


tip_amount = (tip/100) * bill

total_bill_amount = bill + tip_amount
each_bill = total_bill_amount/people
final_each_bill = round(each_bill, 2)
print(f"Each person will pay {final_each_bill}")
