class Vehiculo:
    def __init__(self, combustible, autonomia):
        self.combustible = combustible
        self.autonomia = autonomia
    def que_es(self):
        print("Es un vehículo")


class Coche(Vehiculo):
    def peso_medio(self):
        print("1.5 Toneladas")
    def tamaño(self):
        print("Mediano")
    def que_es(self):
        print("Es un Coche")

class Camion(Vehiculo):
    def peso_medio(self):
        print("2 - 20 Toneladas")
    def tamaño(self):
        print("Grande")
    def que_es(self):
        print("Es un Camión")

class Moto(Vehiculo):
    def peso_medio(self):
        print("100 Kg")
    def tamaño(self):
        print("Pequeño")
    def que_es(self):
        print("Es una Motocicleta")

class Furgoneta(Vehiculo):
    def peso_medio(self):
        print("2.5 Toneladas")
    def tamaño(self):
        print("Mediano - Grande")
    def que_es(self):
        print("Es una Furgoneta")

class Tractor(Vehiculo):
    def peso_medio(self):
        print("2 Toneladas")
    def tamaño(self):
        print("Mediano - Grande")
    def que_es(self):
        print("Es un Tractor")


def Programa_Principal():
    b = [
        Coche("Sin Plomo", "700Km"),
        Camion("Eléctrico", "500Km"),
        Moto("Eléctrico", "50Km"),
        Furgoneta("Diesel", "600Km"),
        Tractor("Diesel", "300Km")]

    for e in b:
        e.que_es()
        e.peso_medio()
        e.tamaño()