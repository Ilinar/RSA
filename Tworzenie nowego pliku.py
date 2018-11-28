#Dodawanie tekstu do tekstu z pliku i tworzenie nowego pliku z nową zawartością.

#nie czyści nowego pliku.

# trzeba zmienić:
# "pliktxt = list(pliktxt)
#   pliktxt.remove('.')
#   pliktxt.remove('t')
#   pliktxt.remove('x')
#   pliktxt.remove('t')
#   plik = ''.join(pliktxt)"
# na coś uniwersalnego.

def edytujplik(pliktxt):
    
    staryplik = open(pliktxt)
    try:
        starypliktekst = staryplik.read()
    finally:
        staryplik.close()
    
    pliktxt = list(pliktxt)
    pliktxt.remove('.')
    pliktxt.remove('t')
    pliktxt.remove('x')
    pliktxt.remove('t')
    plik = ''.join(pliktxt)
    
    nowyplik = open(plik + 'test5.txt', 'a')
    
    nowyplik.write(starypliktekst)
    nowyplik.write('test udany')
    
    nowyplik.close()
      
edytujplik('plik.txt')
