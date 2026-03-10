class Jugador:
    def __init__(self, nombre, diamantes):
        self.nombre = nombre
        self.diamantes = diamantes

    def stacks(self):
        return self.diamantes // 64


class ServidorMinecraft:
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        if len(self.jugadores) < 10:
            self.jugadores.append(jugador)
        else:
            print("Servidor lleno")

    def mostrar_stacks(self):
        for j in self.jugadores:
            print(j.nombre, j.stacks())

    def jugador_mas_diamantes(self):
        mayor = self.jugadores[0]
        for j in self.jugadores:
            if j.diamantes > mayor.diamantes:
                mayor = j
        print(mayor.nombre)

    def total_diamantes(self):
        total = 0
        for j in self.jugadores:
            total += j.diamantes
        print(total)


servidor = ServidorMinecraft()

servidor.agregar_jugador(Jugador("Steve", 130))
servidor.agregar_jugador(Jugador("Alex", 65))
servidor.agregar_jugador(Jugador("Herobrine", 200))

servidor.mostrar_stacks()
servidor.jugador_mas_diamantes()
servidor.total_diamantes()