import tkinter
from tkinter import *
from tkinter import ttk
import random
from tkinter import PhotoImage
from functools import partial
from tkinter import messagebox
from PIL import Image,ImageTk

class Pantalla_inicio:
    
    def __init__(self):
        self.ventana1 = Tk()
        self.ventana1.title("Dificultad")
        self.ventana1.geometry('250x150')
        self.ls_des = ttk.Combobox(self.ventana1, width=17)
        self.ls_des.place(x=48, y=77)
        opciones = ["Facil(5x5)", "Medio(15x15)", "Avanzado(30x30)"]
        self.ls_des['values'] = opciones
        self.boton = ttk.Button(text="Jugar", command=self.iniciarJuego)
        self.boton.place(x=80, y=100)
        self.ventana1.mainloop()
        

    def iniciarJuego(self):
        self.boton
        nivel = self.ls_des.get()
        niveles = {
            'Facil(5x5)': 5,
            'Medio(15x15)': 15,
            'Avanzado(30x30)': 30
        }

        alto = niveles[nivel]
        ancho = alto
        cant_minas = (alto * ancho) // 5
        t = Tablero(alto,ancho,cant_minas)
            
class Tablero:
    
    def __init__(self, alt , anc, nas):
        self.alto = alt
        self.ancho = anc
        self.minas = 0
        self.ventana = Tk()
        self.tabla = []
        self.lista_minas = []
        self.cant_minas = nas
        self.sortear_minas()
        img = Image.open('bandera.jpg')
        img = img.resize((38,38), Image.Resampling.LANCZOS)
        print(img)
        self.imagen = ImageTk.PhotoImage(img, master = self.ventana)
        print(self.imagen)
        self.gano =  0 # 0=jugando 1=perdio 2= gano
        self.conteo = 0
        for j in range(0, self.alto):
                self.lista = []
                for i in range(0, self.ancho):
                    boton = tkinter.Button(self.ventana, height=2, width=2, command=partial(self.apretar, j, i))
                    boton.grid(row=j, column=i)
                    boton.bind("<Button-3>", partial(self.click_derec, j, i))
                    self.lista.append(boton)
                self.tabla.append(self.lista)
        self.ventana.mainloop()
        

    def apretar(self, j, i):
        while self.hay_minas(j,i) and self.conteo == 0: #si hay una minas la primera vez que tocas, sortea de nuevo
                    self.lista_minas = []
                    self.sortear_minas()
        texto = self.tabla[j][i].cget("text")
        if not texto and self.gano == 0:
            self.minas = 0
            b = self.tabla[j][i]
            if self.hay_minas(j, i):
                print("perdio")
                self.gano=1
                self.ventana.withdraw()
                messagebox.showinfo( message="Mejor suerte para la proxima :)", title="Perdiste")
            else:
                self.conteo +=1
                self.minas = self.contar_minas(j, i)
                if self.minas > 0:
                    b.config(text=self.minas)
                else:
                    b.config(text="")
                    
                b.config(relief=tkinter.SUNKEN)
                b.config(bg='silver')
                
    def sortear_minas(self):
        while len(self.lista_minas) < self.cant_minas:
            x = random.randint(0, self.ancho - 1)
            y = random.randint(0, self.alto - 1)
            l = [x, y]
            if l not in self.lista_minas:
                self.lista_minas.append(l)
        print(self.lista_minas)
        return self.lista_minas

    def contar_minas(self, x, y):
        self.minas = 0
        for a in range(x - 1, x + 2):
            for b in range(y - 1, y + 2):
                if [a, b] in self.lista_minas:
                    self.minas += 1
        return self.minas

    def hay_minas(self, x, y):
        return [x, y] in self.lista_minas

    def click_derec(self, j, i, event):
        if self.gano == 0:
            texto = self.tabla[j][i].cget("text")
            if texto:
                self.tabla[j][i].config(text="", image = "", height=2, width=2)
            else:
                self.tabla[j][i].config(text = "P", image=self.imagen, height=38, width=38)
            
            
if __name__ == "__main__":
    juego = Pantalla_inicio()
