import random

def randomprime():
    num = random.randrange(100,1000)
    for i in range(2,num):
        if (num % i) == 0:
            randomprime()
            break
    else:
        print(num)
        
randomprime()
