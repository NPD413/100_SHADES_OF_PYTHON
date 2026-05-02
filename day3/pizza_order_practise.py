print("congratulations,you've got a job at python pizza")
size=input("what size pizza do you want? S ,M or L:")
pepperoni=input("do you want pepporoni on your pizza? Y OR N:")
extra_cheese=input("do you want extra cheese? Y or N:")
price=0
if size=="S":
    price=15
elif size=="M":
    price=20
elif size=="L":
    price==25
if pepperoni=="Y":
    if size=="S":
        price+=2
    elif size=="M" or size=="L":
        price+=3
if extra_cheese=="Y":
    price+=1
print(price)