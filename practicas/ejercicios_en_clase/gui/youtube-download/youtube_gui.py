import tkinter as tk
from tkinter import ttk
from pytube import YouTube


class Checkbox(ttk.Checkbutton):
    '''
    Define un checkbox para elegir bajar solo el audio.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.variable = tk.BooleanVar(self)
        self.configure(variable=self.variable)
    
    def checked(self):
        return self.variable.get()
    
    def check(self):
        self.variable.set(True)
    
    def uncheck(self):
        self.variable.set(False)


class Aplicacion(ttk.Frame):

    ANCHO=400
    ALTO=140

    def __init__(self, parent):
        super().__init__(parent)

        self.tag_url = ttk.Label(
            parent, text="URL video:")

        self.tag_url.place(x=20, y=20)
        self.input_url = ttk.Entry(parent)

        self.input_url.place(x=90, y=20, width=280)

        self.tag_status = ttk.Label(
            parent, text="")
        self.tag_status.place(x=20, y=80)

        # No es necesario crear una variable.
        self.checkbox = Checkbox(self,
            text="Solo audio:", command=self.check_clicked)
        self.checkbox.place(x=20, y=50)

        self.place(width=300, height=200)

        # Boton
        self.boton_descargar = ttk.Button(
            parent, text="Descargar", command=self.descargar)
        # Ubicación boton
        self.boton_descargar.place(x=20, y=100)

    def check_clicked(self):
        print(self.checkbox.checked())

    def descargar(self):
        try:
            CARPETA = "./"  
            link = self.input_url.get()

            yt = YouTube(link)

            d_video = None

            if self.checkbox.checked():
                d_video=yt.streams.filter(only_audio=True).first()
            else:
                d_video = yt.streams.get_by_itag(22)

            d_video.download(CARPETA)

            self.tag_status.config(
                text=f"DESCARGADO!")
   
        except:
            self.tag_status.config(
            text=f"ERROR!...")


# Programa
if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.title("Descargador de Videos de YT del CFP")
    ventana.config(width=Aplicacion.ANCHO, height=Aplicacion.ALTO)

    app = Aplicacion(ventana)
    ventana.mainloop()