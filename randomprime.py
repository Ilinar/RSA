import random
def randomprime():
    global primenum
    primenum= random.randrange(20, 200)
    
    for i in range(2, primenum):
        if primenum % i == 0:
            randomprime()
            break
    else:
        return

    

randomprime()
print(primenum)
p=primenum

randomprime()
print(primenum)
q=primenum
