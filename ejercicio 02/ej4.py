class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.costo_pasaje = 1.50
        self.total_recaudado = 0

    def subir_pasajeros(self, cantidad):
        if self.pasajeros + cantidad <= self.capacidad:
            self.pasajeros += cantidad
            print(self.pasajeros)
        else:
            print("No hay suficientes asientos")

    def cobrar_pasaje(self):
        self.total_recaudado = self.pasajeros * self.costo_pasaje
        print(self.total_recaudado)

    def asientos_disponibles(self):
        print(self.capacidad - self.pasajeros)


bus1 = Bus(40)
bus1.subir_pasajeros(15)
bus1.cobrar_pasaje()
bus1.asientos_disponibles()