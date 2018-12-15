# brakuje funkcji zmieniającej tekst jawny w szyfrogram.

szyfrogram='test udany'

def szyfruj(plikjawny,plikszyfrogram):
    staryplik = open(plikjawny)
    try:
        jawny = staryplik.read()
    finally:
        staryplik.close()
    
    nowyplik = open(plikszyfrogram, 'a')
    nowyplik.write(szyfrogram)
    nowyplik.close()
    
szyfruj('plik.txt','zaszyfrowanyplik.txt')
