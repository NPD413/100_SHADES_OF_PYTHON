"""welcome to the tip calculator! 
what was the total bill? $124.56
how much tip would you like to give? 10, 12, or 15? :12
how many people to split the bill? 7
each person should pay: $19.93"""

print("Welcome to the tip calculator!")
total_bill=float(input("what was the total bill? "))
tips=int(input("how much tip would you like to give {10, 12 or 15}?"))
total_people=int(input("how many people to split the bill?"))
v= tips/100
f=total_bill*v
c=total_bill+f
d=c/total_people
final_amount=round(d,2)
print(f"each person shouold pay:{final_amount}")
      