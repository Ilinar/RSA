import tkinter

window = tk.Tk()
window.title('RSA')
key = tk.Button(window, text = 'Tworzenie pary kluczy', background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white')
key.pack()
szyfrowanie = tk.Button(window, text = 'Szyfrowanie', background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white')
szyfrowanie.pack()
szyfrogram = tk.Button(window, text = 'Czytaj szyfrogram', background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white')
szyfrogram.pack()
exit = tk.Button(window, text = 'Wyjście', background = 'black', activebackground = 'grey', foreground = 'white', activeforeground = 'white')
exit.pack()

tekst = tk.StringVar()


tk.mainloop()
