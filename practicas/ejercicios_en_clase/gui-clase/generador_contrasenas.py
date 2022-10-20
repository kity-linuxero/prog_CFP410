import tkinter as tk
from tkinter import ttk
import contras

# Dimensiones de la ventana (en píxeles)
ANCHO=400
ALTO=150

# Definimos app
app = tk.Tk()
app.title("Ejemplo clase generador contraseña")
app.config(width=ANCHO, height=ALTO)
app.resizable(0, 0)

# Definimos el texto
text1 = ttk.Label(text="Longitud de la contraseña: ")
text1.place(x=20,y=20)

# Definimos input
text_input = ttk.Entry()
#text_input.insert(0,"Escriba su nombre")
text_input.place(x=200, y=20)


contra = tk.StringVar()

# Función para saludar. Crea un nuevo label
def generator():

    if len(text_input.get()):

        try:
            cantidad = int(text_input.get())
        except:
            contra.set("ERROR!. Ingrese un número.")

        contra.set(contras.generador_contraseñas(cantidad))
    else:
        contra.set(contras.generador_contraseñas(6))

btn_saludo = ttk.Button(text="Generar contraseña", command=generator)
btn_saludo.place(x=20,y=50)

text_saludo = ttk.Label(app, textvariable = contra)
text_saludo.place(x=20,y=100)

# Loop de la aplicación
app.mainloop()