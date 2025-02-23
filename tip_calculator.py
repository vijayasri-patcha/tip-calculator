print("welcome to tip calculator")
bill=float(input("what was the total bill? $"))
tip_pre=float(input("What percentage of tip you would like to give?10 12 15"))
people=int(input("How many people you want to split the bill?"))
tip=(tip_pre/100)*bill
total_bill=bill+tip120
bill_per_pers=total_bill/people
final=round(bill_per_pers,2)
print("Each person should pay:",final)
