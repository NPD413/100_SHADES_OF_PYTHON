names=["deepak","dharani"]
for i in names:
    print(names)
    print(names*5)

"""to find the max student marks in an list using for loops"""
student_score=[12,45,67,89,45,23,4,5,567,876]
max_value=0
for i in student_score:
    if i>max_value:
        max_value=i
print(max_value)

"""we use an range function to iterate through the integers"""
for i in range(1,10,3):
    print(i)

count=0
for v in range(1,101):
    count+=v
print(count)