class Videojuego:

    def __init__(self, nombre, plataforma, jugadores=1):
        self.nombre = nombre
        self.plataforma = plataforma
        self.jugadores = jugadores


    def agregar_jugadores(self, cantidad=None):
        if cantidad is None:
            self.jugadores =self.jugadores+ 1
        else:
            self.jugadores = self.jugadores+cantidad

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Plataforma:", self.plataforma)
        print("Cantidad de jugadores:", self.jugadores)
        print("-----------------------")


v1 = Videojuego("FIFA", "PlayStation")
v2 = Videojuego("Minecraft", "PC", 2)

v1.agregar_jugadores()

cantidad = int(input("Ingrese cantidad de jugadores a agregar: "))
v2.agregar_jugadores(cantidad)

v1.mostrar()
v2.mostrar()