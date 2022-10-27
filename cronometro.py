from datetime import datetime
import tkinter as tk


class Cronometro:
    def __init__(self, ventana):
        self.INTERVALO_REFRESCO = 500  # En milisegundos
        self.hora_inicio = datetime.now()
        self.raiz = ventana
        self.variable_hora_actual = tk.StringVar(self.raiz, value= self.obtener_tiempo_transcurrido_formateado())
        self.raiz.etiqueta = tk.Label(
            self.raiz, textvariable= self.variable_hora_actual, font=f"Consolas 60")
        self.raiz.etiqueta.pack(side="top")
        app = tk.Frame()
        self.refrescar_tiempo_transcurrido()
        app.pack()


    def segundos_a_segundos_minutos_y_horas(self, segundos):
        horas = int(segundos / 60 / 60)
        segundos -= horas*60*60
        minutos = int(segundos/60)
        segundos -= minutos*60
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    def obtener_tiempo_transcurrido_formateado(self):
        segundos_transcurridos= (datetime.now() - self.hora_inicio).total_seconds()
        return self.segundos_a_segundos_minutos_y_horas(int(segundos_transcurridos))


    def refrescar_tiempo_transcurrido(self):
        print("Refrescando!")
        self.variable_hora_actual.set(self.obtener_tiempo_transcurrido_formateado())
        self.raiz.after(self.INTERVALO_REFRESCO, self.refrescar_tiempo_transcurrido)


