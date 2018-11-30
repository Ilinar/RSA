def liczby(jawny):
    liczby = []
    lista = list(jawny)
    for i in range(len(lista)):
        liczby.append(ord(lista.pop(0)))
        
    print(liczby)
    
liczby('Ala ma kota')
