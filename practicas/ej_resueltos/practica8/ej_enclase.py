class Encendedor:
    max_capacidad = 10

    def __init__(self, un_color) -> None:
        self.tanque = Encendedor.max_capacidad
        self.color = un_color
        self.encendido = False

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("El encendedor se ha apagado.")
        else:
            print("El encendedor ya está apagado.")

    def encender(self):
        if self.encendido:
            print("Ya está encendido.")
        else:
            if self.tanque > 0:
                self.tanque = self.tanque - 1
                print("Encendedor encendido")
            else:
                print("No hay suficiente carga para un encendido.")

    def recargar(self):
        self.tanque = Encendedor.max_capacidad
        print("Carga al 100%")

# Instanciamos la clase
encendedor1 = Encendedor('Rojo')

for i in range(15):
    encendedor1.encender()
    encendedor1.apagar()

encendedor1.recargar()

encendedor1.encender()






    


    