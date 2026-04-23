print("welcome to the rollercoster!")
height=int(input("enter the height in cm:"))
if height >=  120:
    print("allowed for the ride")
else:
    print("sorry you have to grow taller before you can ride")

print("odd or even")
num=int(input("enter the number:"))
if num%2==0:
    print("even")
else:
    print("odd")

#nested if statements which contains an if statement inside an if 
print("welcome to the ride")
height=int(input("enter the height:"))
bill=0
if height>120:
    print("you can ride")
    age=int(input("enter the age:"))
    if age>=18:
        bill=3
        print("charge for ticket is 7")
    elif age<=18:
        bill=7
        print("charge for ticket is 2")
    photo=input("do you require a photo y or n")
    if photo=="y":
        bill+=5
        print(f"the bill amount is {bill}")
else:
    print("not permitted")