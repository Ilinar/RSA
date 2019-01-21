from tkinter import *
import tkinter as tk
import random
from sys import setrecursionlimit

setrecursionlimit(10000)

def menu():
    """Tworzenie głównego okna."""
    global window
    global bg_image, w, h
    window = tk.Tk()
    window.title('RSA')
    window.iconbitmap(default='key.ico')
    window.geometry('1000x700')

    bg_image = tk.PhotoImage(file='matrix.png')
    w = bg_image.width()
    h = bg_image.height()
    cv = tk.Canvas(width=w, height=h)
    cv.pack(side='top', fill='both', expand='yes')
    cv.create_image(0, 0, image=bg_image, anchor='nw')

    key = tk.Button(cv, text='Tworzenie pary kluczy', command=keymenu, overrelief=RIDGE,
                    background='black', activebackground='grey', foreground='white', activeforeground='white',
                    width=20, font=("Times New Roman", 40))
    key.pack(pady=30)

    szyfrowanie = tk.Button(cv, text='Szyfrowanie', command=szyfrowaniemenu, overrelief=RIDGE,
                            background='black', activebackground='grey', foreground='white', activeforeground='white',
                            width=20, font=("Times New Roman", 40))
    szyfrowanie.pack(pady=30)

    szyfrogram = tk.Button(cv, text='Czytaj szyfrogram', command=deszyfrowaniemenu,overrelief=RIDGE,
                           background='black', activebackground='grey', foreground='white', activeforeground='white',
                           width=20, font=("Times New Roman", 40))
    szyfrogram.pack(pady=30)

    exit = tk.Button(cv, text='Wyjście', command=window.destroy, overrelief=RIDGE,
                     background='black', activebackground='grey', foreground='white', activeforeground='white',
                     width=20, font=("Times New Roman", 40))
    exit.pack(pady=30)
    
    window.bind("<KeyPress-Escape>", zamknij1)

    tk.mainloop()

###############################################################################################################################

def keymenu():
    """Tworzenie okna do generowania kluczy."""
    global windowkey, cvkey, textbox
    global text
    global text2
    windowkey = tk.Toplevel()
    windowkey.title('RSA')

    cvkey = tk.Canvas(windowkey, width=w, height=h)
    cvkey.pack(side='top', fill='both', expand='yes')
    cvkey.create_image(0, 0, image=bg_image, anchor='nw')
    
    exitkey = tk.Button(cvkey, text='Zamknij', command=windowkey.destroy, overrelief=RIDGE,
                     background='black', activebackground='grey', foreground='white', activeforeground='white',
                     width=20, font=("Times New Roman", 40))
    exitkey.pack(pady=30, padx = 30, side = 'bottom', anchor='sw')
    
    keygenerate = tk.Button(cvkey, text="Stwórz klucze", command=printkey,
                            background='black', activebackground='grey', foreground='white', activeforeground='white',
                            width=0, font=("Times New Roman", 60))
    keygenerate.pack(pady=100, side='bottom')

    text = tk.StringVar()
    label = tk.Label(cvkey, textvariable=text,
                     background='black', foreground='white',
                     width=0, font=("Times New Roman", 40))
    # label.pack(side = 'left', padx = 5, pady = 5)
    text.set('Klucz prywatny:')

    text2 = tk.StringVar()
    label2 = tk.Label(cvkey, textvariable=text2,
                      background='black', foreground='white',
                      width=0, font=("Times New Roman", 40))
    # label2.pack(side = 'left', padx = 5, pady = 5)
    text2.set('Klucz publiczny:')

    textbox = Text(cvkey, width=30, height=2,
                   background='black', foreground='white', font=("Times New Roman", 40))
    
    windowkey.bind("<KeyPress-Escape>", zamknij2)

# -----------------------------------------------------------------------------------------------------------------------------#

def randomprime():
    """Losowanie liczby pierwszej."""
    global primenum
    primenum = random.randrange(100, 999)

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
    num = random.randrange(3, n)
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
    fi = (p - 1) * (q - 1)
    global n
    n = p * q
    euclidean()
    global e
    e = num
    ex_euclidean()
    if e == d:
        keygenerate()
        return
    return

def printkey():
    """Wpisywanie kluczy do pola tekstowego."""
    keygenerate()
    se = str(e)
    sd = str(d)
    sn = str(n)
    key = 'klucz publiczny: ' + se + ' ' + sn
    key2 = 'klucz prywatny: ' + sd + ' ' + sn
    text.set(key)
    text2.set(key2)
    textbox.pack(side='top', padx=5, pady=50)
    textbox.delete(1.0, END)
    textbox.insert(tk.END, key, )
    textbox.insert(tk.END, '\n')
    textbox.insert(tk.END, key2, )

###############################################################################################################################

def readkeyszyfruj():
    """Czytanie klucza publicznego wpisanego w pole."""
    global x, y
    klucz = entryklucz.get()
    klucz = klucz.split()
    try:
        x = int(klucz[0])
        y = int(klucz[1])
    except (ValueError, IndexError):
        szyfrogramtekst = 'Błąd. Klucz składa się z dwóch liczb oddzielonych spacją. Spróbuj ponownie.'
        szyfrbox.insert(tk.END, szyfrogramtekst)
        return
    try:
        z = (klucz[2])
        szyfrogramtekst = 'Błąd. Klucz składa się z dwóch liczb oddzielonych spacją. Spróbuj ponownie.'
        szyfrbox.insert(tk.END, szyfrogramtekst)
        return
    except (ValueError, IndexError):
        return
    return

def readkeydeszyfruj():
    """Czytanie klucza prywatnego wpisanego w pole."""
    global x, y
    klucz = entryklucz.get()
    klucz = klucz.split()
    try:
        x = int(klucz[0])
        y = int(klucz[1])
    except (ValueError, IndexError):
        szyfrogramtekst = 'Błąd. Klucz składa się z dwóch liczb oddzielonych spacją. Spróbuj ponownie.'
        szyfrbox.insert(tk.END, szyfrogramtekst)
        return
    try:
        z = (klucz[2])
        szyfrogramtekst = 'Błąd. Klucz składa się z dwóch liczb oddzielonych spacją. Spróbuj ponownie.'
        szyfrbox.insert(tk.END, szyfrogramtekst)
        return
    except (ValueError, IndexError):
        return
    return

###############################################################################################################################

def szyfrowaniemenu():
    """Tworzenie okna do szyfrowania"""
    global window2, entryklucz, entryjawny, szyfrogramtekst, nazwastaregopliku, nazwanowegopliku, szyfrbox
    window2 = tk.Toplevel()
    window2.title('RSA')

    cvszyfrowanie = tk.Canvas(window2, width=w, height=h)
    cvszyfrowanie.pack(side='top', fill='both', expand='yes')
    cvszyfrowanie.create_image(0, 0, image=bg_image, anchor='nw')

    label0 = tk.Label(cvszyfrowanie, text='Podaj klucz:',
                      background='black', activebackground='grey', foreground='white', activeforeground='white',
                      width=10, font=("Times New Roman", 40))
    label0.pack(padx = 5, pady = 5)

    entryklucz = tk.Entry(cvszyfrowanie, background='black', foreground='white', width=25, font=("Times New Roman", 40))
    entryklucz.pack()

    label1 = tk.Label(cvszyfrowanie, text='Tekst jawny:',
                      background='black', activebackground='grey', foreground='white', activeforeground='white',
                      width=10, font=("Times New Roman", 40))
    label1.pack(padx = 5, pady = 5)

    entryjawny = tk.Entry(cvszyfrowanie, background='black', foreground='white', width=95, font=("Times New Roman", 30))
    entryjawny.pack(padx = 5)
    
    okszyfruj = tk.Button(cvszyfrowanie, text='Szyfruj', command=szyfruj,
                          background='black', activebackground='grey', foreground='white', activeforeground='white',
                          width = 20, font=("Times New Roman", 30))
    okszyfruj.pack(pady=5)

    szyfrbox = Text(cvszyfrowanie, width=95, height=3,
                    background='black', foreground='white', font=("Times New Roman", 30), wrap = 'word')
    szyfrbox.insert(tk.END, 'Tutaj zobaczysz szyfrogram')
    szyfrbox.pack(padx = 5)
    
    label2 = tk.Label(cvszyfrowanie, text='Nazwa pliku z tekstem jawnym:',
                      background='black', activebackground='grey', foreground='white', activeforeground='white',
                      width=23, font=("Times New Roman", 40))
    label2.pack(pady = 5)

    nazwastaregopliku = tk.Entry(cvszyfrowanie, background='black', foreground='white', width=25,
                                 font=("Times New Roman", 40))
    nazwastaregopliku.pack()
    
    label3 = tk.Label(cvszyfrowanie, text='Nazwa pliku z szyfrogramem:',
                      background='black', activebackground='grey', foreground='white', activeforeground='white',
                      width = 23, font=("Times New Roman", 40))
    label3.pack(pady = 5)

    nazwanowegopliku = tk.Entry(cvszyfrowanie, background='black', foreground='white', width=25,
                                font=("Times New Roman", 40))
    nazwanowegopliku.pack()

    okszyfrujplik = tk.Button(cvszyfrowanie, text='Szyfruj plik', command=szyfrujplik,
                              background='black', activebackground='grey', foreground='white', activeforeground='white',
                              width = 20, font=("Times New Roman", 30))
    okszyfrujplik.pack(pady = 5)
    
    exitszyfrowanie = tk.Button(cvszyfrowanie, text='Zamknij', command=window2.destroy, overrelief=RIDGE,
                     background='black', activebackground='grey', foreground='white', activeforeground='white',
                     width=20, font=("Times New Roman", 40))
    exitszyfrowanie.pack(pady=30, padx = 30, anchor='sw')
    
    window2.bind("<KeyPress-Escape>", zamknij3)

# -----------------------------------------------------------------------------------------------------------------------------#

def wliczby(jawny):
    """Zamiana teksu jawnego na jawny ciąg liczb."""
    global liczby
    liczby = []
    lista = list(jawny)
    for i in range(len(lista)):
        liczby.append(ord(lista.pop(0)))
    return

def wszyfrogram(liczby):
    """Zamiana jawnego ciągu liczb na szyfrogram."""
    global szyfrogram
    szyfrogram = [(t ** e) % n for t in liczby]
    return

# -----------------------------------------------------------------------------------------------------------------------------#

def szyfruj():
    """Szyfrowanie tekstu z pola tekstowego."""
    szyfrbox.delete(1.0, END)
    readkeyszyfruj()
    global e, n, szyfrogram
    e = x
    n = y
    wliczby(entryjawny.get())
    wszyfrogram(liczby)
    szyfrogram = ' '.join(map(str, szyfrogram))
    szyfrogramtekst = szyfrogram
    szyfrbox.insert(tk.END, szyfrogramtekst)

# -----------------------------------------------------------------------------------------------------------------------------#

def szyfrujplik():
    """Szyfrowanie tekstu z pliku tekstowego."""
    readkeyszyfruj()
    global e, n, szyfrogram
    e = x
    n = y
    staryplik = nazwastaregopliku.get()
    nowyplik = nazwanowegopliku.get()

    try:
        plikjawny = open(staryplik)
        jawny = plikjawny.read()
    finally:
        plikjawny.close()

    wliczby(jawny)
    wszyfrogram(liczby)
    szyfrogram = ' '.join(map(str, szyfrogram))
    szyfrogramtekst = szyfrogram

    try:
        zaszyfrowanyplik = open(nowyplik, 'w')
        zaszyfrowanyplik.write(szyfrogramtekst)
    finally:
        zaszyfrowanyplik.close()

###############################################################################################################################

def deszyfrowaniemenu():
    """Tworzenie okna do czytania szyfrogramu."""
    global window3, entryklucz, entryszyfrogram, jawnybox, szyfrogramtekst, nazwastaregopliku2, nazwanowegopliku2
    window3 = tk.Toplevel()
    window3.title('RSA')

    cvdeszyfrowanie = tk.Canvas(window3, width=w, height=h)
    cvdeszyfrowanie.pack(side='top', fill='both', expand='yes')
    cvdeszyfrowanie.create_image(0, 0, image=bg_image, anchor='nw')

    label0 = tk.Label(cvdeszyfrowanie, text='Podaj klucz:',
                      background='black', activebackground='grey', foreground='white', activeforeground='white',
                      width=10, font=("Times New Roman", 40))
    label0.pack(padx = 5, pady = 5)

    entryklucz = tk.Entry(cvdeszyfrowanie, background='black', foreground='white', width=25, font=("Times New Roman", 40))
    entryklucz.pack()

    label1 = tk.Label(cvdeszyfrowanie, text='Szyfrogram:',
                      background='black', activebackground='grey', foreground='white', activeforeground='white',
                      width=10, font=("Times New Roman", 40))
    label1.pack(padx = 5, pady = 5)

    entryszyfrogram = tk.Entry(cvdeszyfrowanie, background='black', foreground='white', width=95, font=("Times New Roman", 30))
    entryszyfrogram.pack(padx = 5)
    
    okdeszyfruj = tk.Button(cvdeszyfrowanie, text='Czytaj szyfrogram', command=deszyfruj,
                          background='black', activebackground='grey', foreground='white', activeforeground='white',
                          width = 20, font=("Times New Roman", 30))
    okdeszyfruj.pack(pady=5)

    jawnybox = Text(cvdeszyfrowanie, width=95, height=3,
                    background='black', foreground='white', font=("Times New Roman", 30), wrap = 'word')
    jawnybox.insert(tk.END, 'Tutaj zobaczysz tekst jawny')
    jawnybox.pack(padx = 5)
    
    label2 = tk.Label(cvdeszyfrowanie, text='Nazwa pliku z szyfrogramem:',
                      background='black', activebackground='grey', foreground='white', activeforeground='white',
                      width=23, font=("Times New Roman", 40))
    label2.pack(pady = 5)

    nazwastaregopliku2 = tk.Entry(cvdeszyfrowanie, background='black', foreground='white', width=25,
                                 font=("Times New Roman", 40))
    nazwastaregopliku2.pack()
    
    label3 = tk.Label(cvdeszyfrowanie, text='Nazwa pliku z tekstem jawnym:',
                      background='black', activebackground='grey', foreground='white', activeforeground='white',
                      width = 23, font=("Times New Roman", 40))
    label3.pack(pady = 5)

    nazwanowegopliku2 = tk.Entry(cvdeszyfrowanie, background='black', foreground='white', width=25,
                                font=("Times New Roman", 40))
    nazwanowegopliku2.pack()

    okdeszyfrujplik = tk.Button(cvdeszyfrowanie, text='Czytaj plik', command = deszyfrujplik,
                              background='black', activebackground='grey', foreground='white', activeforeground='white',
                              width = 20, font=("Times New Roman", 30))
    okdeszyfrujplik.pack(pady = 5)
    
    exitdeszyfrowanie = tk.Button(cvdeszyfrowanie, text='Zamknij', command=window3.destroy, overrelief=RIDGE,
                     background='black', activebackground='grey', foreground='white', activeforeground='white',
                     width=20, font=("Times New Roman", 40))
    exitdeszyfrowanie.pack(pady=30, padx = 30, anchor='sw')
    
    window3.bind("<KeyPress-Escape>", zamknij4)

# ------------------------------------------------------------------------------------------------------------------------------#

def wjawny(szyfrogram):
    """Zamiana szyfrogramu w liczby jawne"""
    szyfrogram = szyfrogram.split()
    szyfrogram = [int(i) for i in szyfrogram]
    global liczby
    liczby = [(c**d) % n for c in szyfrogram]
    return

def zliczby(jawneliczby):
    """Zamiana liczb jawnych na tekst jawny"""
    global jawny
    jawny = []
    for i in range(len(jawneliczby)):
        jawny.append(chr(jawneliczby.pop(0)))
    return

# ------------------------------------------------------------------------------------------------------------------------------#

def deszyfruj():
    """Deszyfrowanie tekstu w polu tekstowym"""
    jawnybox.delete(1.0, END)
    readkeydeszyfruj()
    global d, n, jawny
    d = x
    n = y
    wjawny(entryszyfrogram.get())
    zliczby(liczby)
    jawny = ''.join(map(str, jawny))
    jawnytekst = jawny
    jawnybox.insert(tk.END, jawnytekst)

# ------------------------------------------------------------------------------------------------------------------------------#

def deszyfrujplik():
    """Deszyfrowanie tekstu w pliku tekstowym"""
    readkeydeszyfruj()
    global d, n, jawny
    d = x
    n = y
    staryplik2 = nazwastaregopliku2.get()
    nowyplik2 = nazwanowegopliku2.get()

    try:
        plikzaszyfrowany = open(staryplik2)
        szyfrogram = plikzaszyfrowany.read()
    finally:
        plikzaszyfrowany.close()

    wjawny(szyfrogram)
    zliczby(liczby)
    jawny = ''.join(map(str, jawny))
    jawnytekst = jawny

    try:
        odszyfrowanyplik = open(nowyplik2, 'w')
        odszyfrowanyplik.write(jawnytekst)
    finally:
        odszyfrowanyplik.close()

###############################################################################################################################

def zamknij1(event):
    """Funkcja zamykająca główne okno"""
    window.destroy()

def zamknij2(event):
    """Funkcja zamykająca okno tworzenia kluczy"""
    windowkey.destroy()
    
def zamknij3(event):
    """Funkcja zamykająca okno do szyfrowania"""
    window2.destroy()
    
def zamknij4(event):
    """Funkcja zamykająca okno do czytania szyfru"""
    window3.destroy()
    
###############################################################################################################################   
    
menu()
