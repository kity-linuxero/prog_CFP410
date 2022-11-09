import tkinter as tk
from tkinter import StringVar, ttk, messagebox, filedialog, font, Button
from pytube import YouTube
from yt_core import download_audio, download_video, DurationError, RICK_VIDEO
from custom_checkbox import Checkbox

ANCHO=400
ALTO=240

class Aplicacion(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        # Tag URL video

        self.tag_url = ttk.Label(
            parent, text="URL video:",font=("Arial", 18))
        self.tag_url.grid(pady=10)
        
        self.folder_name = './'

        #Entry Box
        self.input_urlVar = StringVar()
        self.input_url = ttk.Entry(parent,width=50,textvariable=self.input_urlVar, font=("Arial", 10))
        self.input_url.grid(padx=10)
        self.input_urlVar.set(RICK_VIDEO)
        
        self.checkbox = Checkbox(parent,
             text="Solo audio", command=self.check_clicked)

        self.checkbox.grid(pady=5)

        #myFont = font(family='Helvetica')
        
        # Botón elegir carpeta
        self.saveEntry = Button(parent,width=40,text="Elegir carpeta",command=self.openLocation, bg='#0052cc', fg='white', font=('Arial',12))
        
        self.saveEntry.grid(pady=5)

        # Boton de descarga
        self.boton_descargar = Button(
            parent,width=40, text="Descargar", command=self.descargar, bg='green', fg='white', font=('Arial',12)
            ).grid(pady=5)


    def check_clicked(self):
        print(self.checkbox.checked())

    # file location
    def openLocation(self):
        #global Folder_Name
        self.folder_name = filedialog.askdirectory()
        if(len(self.folder_name) > 1):
            #locationError.config(text=self.folder_name,fg="green")
            print(self.folder_name)
        else:
            #locationError.config(text="Please Choose Folder!!",fg="red")
            print("Error folder")
        

    def descargar(self):
        try:          
            link = self.input_urlVar.get()

            print(f"CARPETA: {self.folder_name}")

            if self.checkbox.checked():
                download_audio(link, self.folder_name)
            else:
                download_video(link, self.folder_name)
            messagebox.showinfo("Joya!", "¡Video Descargado!")
        except DurationError:
            messagebox.showerror("Error", "Video demasiado largo.")
        except Exception as e:
            messagebox.showerror("Error", "ERROR en la descarga!")
            print(e)

# Programa
if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.title("Descargador de Videos de YT del CFP")
    ventana.config(width=ANCHO, height=ALTO)
    #ventana.geometry(f"{ANCHO}x{ALTO}")
    ventana.columnconfigure(0,weight=1)#set all content in center.

    app = Aplicacion(ventana)
    ventana.mainloop()