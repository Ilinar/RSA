def wliczby(jawny):
    liczby = []
    lista = list(jawny)
    for i in range(len(lista)):
        liczby.append(ord(lista.pop(0)))
    return(liczby)

def szyfruj(plikjawny,plikszyfrogram):
    staryplik = open(plikjawny)
    try:
        jawny = staryplik.read()
    finally:
        staryplik.close()
    
    liczby = ' '.join(map(str,wliczby(jawny)))
    
    try:
        nowyplik = open(plikszyfrogram, 'w')
        nowyplik.write(liczby)
    finally:
        nowyplik.close()
