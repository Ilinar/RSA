import random
def randomprime():
    global primenum
    primenum= random.randrange(10, 20)
    
    for i in range(2, primenum):
        if primenum % i == 0:
            randomprime()
            break
    else:
        return
    
def diffrentnum():
    global q
    randomprime()
    q = primenum
    if q == p:
        diffrentnum()
    else:
        return

def keygenerate():
    randomprime()
    global p
    p = primenum
    diffrentnum()
    print (p , q)
    global fi
    fi = (p-1) * (q-1)
    global n
    n = p * q
    print (fi, n)
    
keygenerate()
