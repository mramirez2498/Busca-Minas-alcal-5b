from tkinter import *
from tkinter import ttk
import random
from functools import partial
from tkinter import messagebox
from PIL import Image,ImageTk
import time
from cronometro import Cronometro

class Pantalla_inicio:
    
    def __init__(self):
        
        self.ventana1 = Tk()
        self.ventana1.title("Dificultad")
        self.ventana1.geometry('350x300') #Tamaño de la pantalla de inicio
        self.ls_des = ttk.Combobox(self.ventana1, width=17, state='readonly')
        self.ls_des.set ('Facil(5x5)')
        self.ls_des.place(x=100, y=235) #Posicion de la lista desplegable
        opciones = ["Facil(5x5)", "Medio(15x15)", "Avanzado(20x20)"]
        self.ls_des['values'] = opciones
        self.boton = ttk.Button(text="Jugar", command=self.iniciarJuego)
        self.boton.place(x=130, y=260) #Posicion del boton "jugar"
        self.f20 = Frame(self.ventana1, width=250,height=150)
        self.f20.pack(side="top") #Posicion de la imagen 
        img = PhotoImage(file = "bomba.png")
        men_img = Label(self.f20, image = img)
        men_img.pack()
        self.ventana1.mainloop()
     
    def iniciarJuego(self):
        self.boton
        nivel = self.ls_des.get()
        niveles = {
            'Facil(5x5)': 5,
            'Medio(15x15)': 15,
            'Avanzado(20x20)': 20
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
        self.frameContador = Frame(self.ventana)
        self.frameBotones = Frame(self.ventana)
        self.frameContador.grid(column=0, row=0)
        self.frameBotones.grid(column=0, row=1)
        self.cron = Cronometro(self.frameContador)
        img = Image.open('bandera.png')
        img = img.resize((38,38), Image.Resampling.LANCZOS)
        #print(img)
        self.imagen = ImageTk.PhotoImage(img, master = self.ventana)
        #print(self.imagen)
        self.gano =  0 # 0=jugando 1=perdio 2= gano
        self.conteo = 0
        for j in range(0, self.alto):
                self.lista = []
                for i in range(0, self.ancho):
                    boton = Button(self.frameBotones, height=2, width=2, command=partial(self.apretar, j, i))
                    boton.grid(row=j, column=i)
                    boton.bind("<Button-3>", partial(self.click_derec, j, i))
                    self.lista.append(boton)
                self.tabla.append(self.lista)
        self.ventana.mainloop()
        
        
    def apretar(self, j, i):
        
        if i>=0 and i<self.ancho and j>=0 and j<self.alto and self.tabla[j][i].cget("relief") == RAISED:
            #print(f"row:{j} col:{i}")
            while self.hay_minas(j,i) and self.conteo == 0: #si hay una minas la primera vez que tocas, sortea de nuevo
                self.lista_minas = []
                self.sortear_minas()
            texto = self.tabla[j][i].cget("text")
            if not texto and self.gano == 0:
                minas = 0
                b = self.tabla[j][i]
                if self.hay_minas(j, i):
                    #print("perdio")
                    self.gano=1
                    self.ventana.withdraw()
                    messagebox.showinfo( message="Mejor suerte para la proxima :)", title="Perdiste")
                else:
                    b.config(relief=SUNKEN)
                    b.config(bg='silver')
                    self.conteo +=1
                    minas = self.contar_minas(j, i)
                    if minas > 0:
                        b.config(text=minas)
                    else:
                        b.config(text="")
                        self.apretar(j,i+1)
                        self.apretar(j,i-1)
                        self.apretar(j+1, i)
                        self.apretar(j-1, i)
                        self.apretar(j+1, i+1)
                        self.apretar(j-1, i-1)
                        self.apretar(j+1, i-1)
                        self.apretar(j-1, i+1)
                
    def sortear_minas(self):
        while len(self.lista_minas) < self.cant_minas:
            x = random.randint(0, self.ancho - 1)
            y = random.randint(0, self.alto - 1)
            l = [x, y]
            if l not in self.lista_minas:
                self.lista_minas.append(l)
        #print(self.lista_minas)
        return self.lista_minas

    def contar_minas(self, x, y):
        minas = 0
        for a in range(x - 1, x + 2):
            for b in range(y - 1, y + 2):
                if [a, b] in self.lista_minas:
                    minas += 1
        return minas

    def hay_minas(self, x, y):
        return [x, y] in self.lista_minas

    def click_derec(self, j, i, event):
        if self.tabla[j][i].cget("relief") == RAISED:
            if self.gano == 0:
                texto = self.tabla[j][i].cget("text")
                if texto:
                    self.tabla[j][i].config(text="", image = "", height=2, width=2)
                else:
                    self.tabla[j][i].config(text = "P", image=self.imagen, height=38, width=38)
                    
            
if __name__ == "__main__":
    juego = Pantalla_inicio()
