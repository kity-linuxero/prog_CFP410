'''
Ejercicio hecho en clase el 01/09/22
'''

class Tv:
    CANAL_MAX = 135
    CANAL_MIN = 2
    VOL_MAX = 10
    VOL_MIN = 0

    def __init__(self) -> None:
        self.encendido = False
        self.canal = 2
        self.volumen = 0

    def esta_encendido(self):
        return self.encendido

    def on_off(self):
        if self.esta_encendido():
            self.apagar()
        else:
            self.encender()
    
    def encender(self):
        self.encendido = True
        print ("El TV se ha encendido.")

    def apagar(self):
        self.encendido = False
        print ("El TV se ha apagado.")
            
    def canal_actual(self):
        if self.esta_encendido():
            return self.canal

    def cambiar_a_canal(self, canal):
        if self.esta_encendido():
            if canal <= Tv.CANAL_MAX and canal >= Tv.CANAL_MIN:
                self.canal = canal
                print(f"Se cambió al canal {canal}")
            else:
                print("Canal fuera de rango")
                return False

    def canal_up(self):
        if self.canal_actual() == Tv.CANAL_MAX:
            self.cambiar_a_canal(Tv.CANAL_MIN)
        else:
            self.cambiar_a_canal(self.canal_actual()+1)

    def canal_down(self):
        if self.canal_actual() == Tv.CANAL_MIN:
            self.cambiar_a_canal(Tv.CANAL_MAX)
        else:
            self.cambiar_a_canal(self.canal_actual()-1)

    def volumen_actual(self):
        if self.esta_encendido():
            return self.volumen

    def cambiar_a_volumen(self, un_valor):
        if self.esta_encendido():
            if un_valor <= Tv.VOL_MAX and un_valor >= Tv.VOL_MIN:
                self.volumen = un_valor
                print(f"VOL: {self.volumen_actual()}")
            else:
                print ("Volumen fuera de rango")
                return False

    def volumen_up(self):
        if self.volumen_actual() < Tv.VOL_MAX:
            self.cambiar_a_volumen(self.volumen_actual()+1)
        else:
            print("VOL MAX!")
    
    def volumen_down(self):
        if self.volumen_actual() > Tv.VOL_MIN:
            self.cambiar_a_volumen(self.volumen_actual()-1)
        else:
            print("VOL MIN!")
    

tv1 = Tv()
tv1.on_off()
print(tv1.canal_actual())

tv1.canal_up()
tv1.volumen_up()
tv1.cambiar_a_canal(800)
tv1.cambiar_a_canal(64)
tv1.on_off()





    

