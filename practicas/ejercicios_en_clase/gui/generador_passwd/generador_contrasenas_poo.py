'''
Versión orientada a objetos
'''

import tkinter as tk
from tkinter import ttk

try:
    import contras
    
    # El máximo posible de contraseña. Para que no pueda hacerse una contraseña de infinitos caracteres.
    MAX_LENGTH = 64

    # Dimensiones de la ventana (en píxeles)
    ANCHO=500 
    ALTO=200

    class Application():

        def __init__(self):
            # Definimos app
            self.app = tk.Tk()
            self.app.title("Generador de contraseñas seguras")
            self.app.config(width=ANCHO, height=ALTO)
            self.app.resizable(0, 0) # Para que la ventana no pueda redimensionarse

            # Definimos un texto
            self.text1 = ttk.Label(text=f"Longitud de la contraseña (Max {MAX_LENGTH}):")
            # Posición del texto
            self.text1.place(x=20,y=20) 

            # Definimos input
            self.text_input = ttk.Entry(width=4)
            # Posición del input
            self.text_input.place(x=270, y=20)

            # Variable donde se guardará la contraseña.
            self.contra = tk.StringVar()

            # Texto para avisar que la contraseña se almacenó en el portapapeles
            self.msg = tk.StringVar()

                # El botón para generar contraseñas
            self.btn_gen = ttk.Button(text="Generar contraseña segura", command=self.generator)
            # La ubicación del botón
            self.btn_gen.place(x=20,y=60)

            '''
            El label que contendrá la contraseña
            Observe el parámetro 'textvariable = contra'. Contra es el StringVar. Por lo tanto, el texto cambiará automáticamente cuando se cambie
            el StringVar
            '''
            self.text_contra = ttk.Label(self.app, textvariable = self.contra, font=("Courier New", 12))
            # Ubicación de la contraseña
            self.text_contra.place(x=20,y=110)

            # Mensaje para avisar que la contraseña se guardó en el portapapeles
            self.text_msg_porta = ttk.Label(self.app, textvariable = self.msg)
            # Ubicación del mensaje para avisar que la contraseña se guardó en el portapapeles
            self.text_msg_porta.place(x=20,y=160)
            
            # Loop de la aplicación
            self.app.mainloop()

        def clip(self, text):
            '''
            Copia el parámetro enviado 'text' al portapapeles
            '''
            self.app.clipboard_clear()
            self.app.clipboard_append(text)

        def generator(self):
            '''
            Toma la longitud de la contraseña en el input y la envía a la función que genera la contraseña
            '''
            # Si se encuentra contenido en el input


            try:
                cantidad = abs(int(self.text_input.get())) # abs para convertir negativos en números válidos
                # No hubo excepción. Se espera que muestre la contraseña de longitud 'cantidad'

                if len(self.text_input.get()):
                    contra_generada= ''
                    
                    if cantidad < MAX_LENGTH:
                        contra_generada=(contras.generador_contraseñas(cantidad))
                    else:
                        contra_generada=(contras.generador_contraseñas(MAX_LENGTH))

                else:
                    # No se ingresó ninguna longitud. Por defecto, el programa generará contraseñas de longitud Maxima/4.
                    contra_generada = contras.generador_contraseñas(MAX_LENGTH/3)
            
                self.contra.set(contra_generada)
                self.clip(contra_generada) # Copia la contraseña al portapapeles
                self.msg.set("Se ha guardado la contraseña completa al portapapeles.")

            except Exception as e:
                # Inserta un texto en el StringVar.
                # Si da error al convertir a int lo ingresado, mostrará este mensaje de error.
                self.contra.set("¡ERROR!. Ingrese un número válido.")
                self.msg.set("")
                print(f"ERROR: {e}")


    def main():
        mi_app = Application()

    if __name__ == '__main__':
        main()
except ImportError as e:
    print(f"Error al importar el módulo generador de contraseñas.\nERROR: {e}")
except Exception as e:
    print(f"Ha ocurrido un error inesperado.\nERROR: {e}")
