import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','@','#','$','%','^','&','*']
numbers = ['0','1','2','3','4','5','6','7','8','9']

nr_letters=int(input("how many letters do you like in your password: "))
nr_symbols=int(input("how many symbols would u like:"))
nr_numbers=int(input("how many numbers would you like: "))

""" easy level
password =""
for i in range (1,nr_letters+1):
   password+=random.choice(letters)  

for i in range(1,nr_symbols+1):
   password+=random.choice(symbols)

for i in range(1,nr_numbers+1):
   password+=random.choice(numbers)

print(password)
   """

password =[]
for i in range (1,nr_letters+1):
   password+=random.choice(letters)  

for i in range(1,nr_symbols+1):
   password+=random.choice(symbols)

for i in range(1,nr_numbers+1):
   password+=random.choice(numbers)

random.shuffle(password)
print(password) 

final_password=""
for i in password:
   final_password+=str(i)
print(final_password)