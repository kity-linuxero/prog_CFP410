import tkinter as tk
from tkinter import StringVar, ttk, messagebox, filedialog
from pytube import YouTube
from yt_core import download_audio, download_video

ANCHO=400
ALTO=240


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

    def __init__(self, parent):
        super().__init__(parent)

        # Tag URL video

        self.tag_url = ttk.Label(
            parent, text="URL video:")
        self.tag_url.grid()
        
        self.folder_name = './'

        #self.tag_url.place(x=20, y=20)

        #Entry Box
        self.input_urlVar = StringVar()
        self.input_url = ttk.Entry(parent,width=50,textvariable=self.input_urlVar)
        self.input_url.grid(padx=10)
        


        
        # No es necesario crear una variable.
        #self.checkbox_audio = Checkbox(parent).(text="Solo audio:", command=self.check_clicked).grid(row=1,column=0)

        self.checkbox = Checkbox(parent,
             text="Solo audio", command=self.check_clicked)

        self.checkbox.grid()
        # self.checkbox.place(x=240, y=35)

        # self.checkbutton1=tk.Checkbutton(self,text="C1")
        # self.checkbutton1.grid(row=3,column=3)

        #self.place(width=self.ANCHO, height=self.ALTO)



        
        # Botón elegir carpeta
        self.saveEntry = ttk.Button(parent,text="Elegir carpeta",command=self.openLocation)
        self.saveEntry.grid()

        # Boton de descarga
        self.boton_descargar = ttk.Button(
            parent, text="Descargar", command=self.descargar).grid(pady=5)

        # Status bar
        self.statusvar = StringVar()
        self.statusvar.set("Ready")
        self.sbar = ttk.Label(parent, textvariable=self.statusvar, relief=tk.SUNKEN, anchor="w")
        
        self.sbar.pack(side=tk.BOTTOM, fill=tk.X)
        

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

            print(link)

            #self.status.set("Descargando!...")

            if self.checkbox.checked():
                download_audio(link)
            else:
                download_video(link)

            
            messagebox.showinfo("Error", "Descargado!")
        except Exception as e:
            #self.status.set("ERROR en la descarga")
            messagebox.showerror("Error", "ERROR en la descarga!")
            print(e)
        #self.status.set("Descargado, chabon!...")


# Programa
if __name__ == '__main__':
    ventana = tk.Tk()
    ventana.title("Descargador de Videos de YT del CFP")
    ventana.config(width=ANCHO, height=ALTO)
    ventana.geometry(f"{ANCHO}x{ALTO}")
    ventana.columnconfigure(0,weight=1)#set all content in center.

    app = Aplicacion(ventana)
    ventana.mainloop()