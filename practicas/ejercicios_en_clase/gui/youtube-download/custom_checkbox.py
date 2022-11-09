import tkinter as tk
from tkinter import ttk, BooleanVar

class Checkbox(ttk.Checkbutton):
    '''
    Define un checkbox para elegir bajar solo el audio.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.variable = BooleanVar(self)
        self.configure(variable=self.variable)
    
    def checked(self):
        return self.variable.get()
    
    def check(self):
        self.variable.set(True)
    
    def uncheck(self):
        self.variable.set(False)