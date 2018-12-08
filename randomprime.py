import random

def randomprime():
    num = random.randrange(100, 1000)
    for i in range(2, num):
        if (num % i) == 0:
            randomprime()
        else:
            return num
        
a = randomprime()
print(a)
type(a)
