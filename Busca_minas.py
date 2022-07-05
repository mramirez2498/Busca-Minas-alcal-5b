import tkinter
from tkinter import *
from tkinter import ttk
import random
import pprint
from functools import partial
from tkinter import messagebox

tabla = []
lista_minas = []

def iniciar():
    iniciarJuego(ls_des.get())
   
ventana = Tk()
ventana.title("Dificultad")
ventana.geometry('250x150')
ls_des = ttk.Combobox(ventana,width=17)
ls_des.place(x=30,y=77)
opciones = ["Facil(5x5)","Medio(15x15)","Avanzado(30x30)"]
ls_des['values']=opciones

boton = ttk.Button(text="Jugar",command=iniciar)
boton.place(x=70, y=100)

def iniciarJuego(nivel):
    niveles = {
        'Facil(5x5)':5,
        'Medio(15x15)':15,
        'Avanzado(30x30)':30
        }
    
    alto = niveles[nivel]
    ancho = alto
    cant_minas = (alto * ancho) // 5
    pp = pprint.PrettyPrinter()
    sortear_minas(cant_minas, ancho, alto)
    ventana = tkinter.Tk()
    ventana.title("Busca Minas")
    for j in range(0, alto):
        lista = []
        for i in range(0, ancho):
            boton = tkinter.Button(ventana, height = 2, width = 2, command=partial(apretar, j, i))
            boton.grid(row=j, column=i)
            lista.append(boton)
        tabla.append(lista)
    ventana.mainloop()

def apretar(j, i):
    minas = 0
    b = tabla[j][i]
    if hay_mina(j,i):
        print("perdio")
        messagebox.showinfo(message="Perdiste", title="Perdiste")
        
    else:
        minas = contar_minas(j,i)
    if minas>0:
        b.config(text=minas)
    else:
        b.config(text="")
    b.config(relief=tkinter.SUNKEN)
    b.config(bg='Silver')
    
def sortear_minas(cant_minas, ancho, alto):
    while len(lista_minas) < cant_minas:
        x = random.randint(0, ancho -1)
        y = random.randint(0, alto -1)
        l = [x, y]
        if l not in lista_minas:
            lista_minas.append(l)
    print(lista_minas)
    return lista_minas

def contar_minas(x,y):
    minas = 0
    for a in range(x-1, x+1):
        for b in range(y-1, y+1):
            if [a,b] in lista_minas:
                minas += 1
    return minas

def hay_mina(x,y):
    return [x,y] in lista_minas