#wersja testowa, wyświetla kroki po drodze

import random
def test():
    a = random.randrange(10,20)
    print ('wylosowano ',a)
    for i in range(2,a):
        print ('dzielimy przez ', i)
        if a % i == 0:
            test()
            break

    else:
        print (a, 'jest pierwsza') 
        print(type(a))
        return a

    
  
  
c = test()
print(c)
type(c)


#wersja zwykła

import random

def randomprime():
    num = random.randrange(10, 20)
    for i in range(2, num):
        if num % i == 0:
            randomprime()
            break

    else:
        return num
        
a = randomprime()
print(a)
type(a)
