import random
import my_module
random_integer=random.randint(1,10)
print(random_integer)
print(my_module.my_favourite_no)


"""to random take of an float number"""
random_float=random.random()
print(random_float)

"""print heads or tails at random"""
heads_or_tails=random.randint(0,1)
if heads_or_tails==0:
    print("IT'S HEADS")
else:
    print("IT'S TAILS")