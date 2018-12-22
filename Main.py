import random

def randomprime():
    """Losowanie liczby pierwszej."""
    global primenum
    primenum= random.randrange(100, 200)
    
    for i in range(2, primenum):
        if primenum % i == 0:
            randomprime()
            break
    else:
        return
    
def diffrentnum():
    """Ponowne losowanie w przypadku dwóch identycznych liczb pierwszych."""
    global q
    randomprime()
    q = primenum
    if q == p:
        diffrentnum()
    else:
        return
    
def euclidean():
    """Algorytm Euklidesa, losowanie i dopasowywanie liczby by tworzyć parę licz względnie pierwszych."""
    global num
    num = random.randrange(3,n)
    if num % 2 == 0:
        euclidean()
    else:
        if num == fi:
            euclidean()
        a = num
        b = fi
        while a != b:
            if a > b:
                a = a - b
            elif a < b:
                b = b - a
        if a == b == 1:
            return
        else:
            euclidean()

def ex_euclidean():
    """Rozszerzony algorytm Euklidesa, szukanie odwrotności modulo."""
    global d
    a = e
    b = fi
    u = 1
    x = 0
    w = a
    z = b
    while w != 0:
        if w < z:
            tym = w
            w = z
            z = tym
            tym = u
            u = x
            x = tym
        k = int(w / z)
        u = u - (k * x)
        w = w - (k * z)
    if x < 0:
        x = x + b
    d = x
    return d
    
def keygenerate():
    """Tworzenie pary kluczy."""
    randomprime()
    global p
    p = primenum
    diffrentnum()
    global fi
    fi = (p-1) * (q-1)
    global n
    n = p * q
    euclidean()
    global e
    e = num
    ex_euclidean()
    if e == d:
        keygenerate()
        return
    print('klucz publiczny:', e , n)
    print('klucz prywatny:', d , n)
    return

####################################

def wliczby(jawny):
    """Zamiana teksu jawnego na jawny ciąg liczb."""
    global liczby
    liczby = []
    lista = list(jawny)
    for i in range(len(lista)):
        liczby.append(ord(lista.pop(0)))
    return

def szyfrogram(liczby):
    """Zamiana jawnego ciągu liczb na szyfrogram."""
    global szyfrogram
    szyfrogram = [(t**e) % n for t in liczby]
    return

####################################

def deszyfruj(szyfrogram):
    szyfrogram = szyfrogram.split()
    szyfrogram = [int(i) for i in szyfrogram]
    global liczby
    liczby = [(c**d) % n for c in szyfrogram]
    return

def zliczby(jawneliczby):
    global jawny
    jawny = []
    for i in range(len(jawneliczby)):
        jawny.append(chr(jawneliczby.pop(0)))
    return

####################################

print('Twórz parę kluczy - 1 \nSzyfruj - 2 \nDeszyfruj - 3')
wybierz = int(input())

if wybierz == 1:
    keygenerate()
    
elif wybierz == 2:
    print('Wprowadz klucz publiczny(e,n):')
    print('e')
    e = int(input())
    print('n')
    n = int(input())
    print('Tekst jawny:')
    wliczby(input())
    szyfrogram(liczby)
    szyfrogram = ' '.join(map(str,szyfrogram))
    print(szyfrogram)
    
elif wybierz == 3:
    print('Wprowadz klucz prywatny(d,n):')
    print('d')
    d = int(input())
    print('n')
    n = int(input())
    print('Szyfrogram:')
    deszyfruj(input())
    #liczby = liczby.split()
    zliczby(liczby)
    jawny = ''.join(map(str,jawny))
    print(jawny)
    
else:
    print("Źle prowadzone dane.")
