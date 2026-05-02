list=["apple","orange","grapes","banana"]
list[3]="muskmellon"
print(list)
list.append("watermellon")
print(list[0])
print(list[-1])
print(list[2])

import random
friends=["Alice","Bob","charlie","david","emanuel"]
"""friends=random.randint(0,5)
if friends==0:
    print("Alice")
elif friends==1:
    print("Bob")
elif friends==2:
    print("charlie")
elif friends==3:
    print("david")
else:
    print("emanuel")"""

print(random.choice(friends))

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])