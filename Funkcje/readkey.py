def readkey():
    global x,y
    klucz = input('Wprowadz klucz publiczny e n: ')
    klucz = klucz.split()
    try:
        x = int(klucz[0])
        y = int(klucz[1])
    except (ValueError, IndexError):
        print('Błąd. Klucz składa się z dwóch liczb oddzielonych spacją. Spróbuj ponownie.')
        readkey()
        return
    try:
        z = (klucz[2])
        print('Błąd. Klucz składa się z dwóch liczb oddzielonych spacją. Spróbuj ponownie.')
        readkey()
        return
    except (ValueError, IndexError):
        return
    return
