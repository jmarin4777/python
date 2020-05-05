import random
def randInt(min=0, max=100):
    if min>max:
        print("the maximum boundary must be greater than the minimum boundary.")
    else:
        num = random.random() * (max-min) + min
    return round(num)
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
print(randInt(min=-80, max=-20))
