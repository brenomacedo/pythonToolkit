import webbrowser
from tkinter import *

root = Tk( )

root.title('Abrir browser')
root.geometry('300x200')

def google():
    webbrowser.open('http://www.google.com')

mygoogle = Button(root, text='Abrir o google', command=google).pack(pady = 20)

root.mainloop()