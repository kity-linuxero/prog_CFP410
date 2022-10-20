import tkinter as tk
from tkinter import ttk
import contras

# Dimensiones de la ventana (en píxeles)
ANCHO=400
ALTO=500

# Definimos app
app = tk.Tk()
app.title("Ejemplo clase")
app.config(width=ANCHO, height=ALTO)

# Definimos el texto
text1 = ttk.Label(text="Longitud de la contraseña: ")
text1.place(x=20,y=20)

# Definimos input
text_input = ttk.Entry()
#text_input.insert(0,"Escriba su nombre")
text_input.place(x=160, y=20)

# Función para saludar. Crea un nuevo label
def saludo():

    
    if len(text_input.get()):
        cantidad = int(text_input.get())
        contra = contras.generador_contraseñas(cantidad)
    #print (text_input.get())
    else:
        contra = contras.generador_contraseñas(6)

    text_saludo = ttk.Label(text=contra)
    text_saludo.place(x=20,y=100)

btn_saludo = ttk.Button(text="Saludame", command=saludo)
btn_saludo.place(x=20,y=50)

# Loop de la aplicación
app.mainloop()