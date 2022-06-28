from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter
from Busca_minas import iniciarJuego, sortear_minas
from functools import partial

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