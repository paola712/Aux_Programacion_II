class Animal:
    def __init__(self, nombre, edad, nombreDueno):
        self.nombre = nombre
        self.edad = edad
        self.nombreDueno = nombreDueno


class Perro(Animal):
    def __init__(self, nombre, edad, nombreDueno, requiereBosal, ladraFuerte):
        super().__init__(nombre, edad, nombreDueno)
        self.requiereBosal = requiereBosal
        self.ladraFuerte = ladraFuerte

    def mostrar(self):
        print(f"Perro: {self.nombre}, Edad: {self.edad}, Dueño: {self.nombreDueno}")


class Gato(Animal):
    def __init__(self, nombre, edad, nombreDueno, cazaRatones, tomaLeche):
        super().__init__(nombre, edad, nombreDueno)
        self.cazaRatones = cazaRatones
        self.tomaLeche = tomaLeche

    def mostrar(self):
        print(f"Gato: {self.nombre}, Edad: {self.edad}, Dueño: {self.nombreDueno}")


class CentroVeterinario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.perros = []
        self.gatos = []
        self.cantPerros = 0
        self.cantGatos = 0

    def agregar_perro(self, perro):
        if self.cantPerros < 100:
            self.perros.append(perro)
            self.cantPerros += 1

    def agregar_gato(self, gato):
        if self.cantGatos < 100:
            self.gatos.append(gato)
            self.cantGatos += 1

    # b. Ordenar perros
    def ordenar_perros(self):
        self.perros.sort(key=lambda p: (p.edad, p.nombreDueno, p.nombre))

    # c. Ordenar gatos
    def ordenar_gatos(self):
        self.gatos.sort(key=lambda g: (
            not g.tomaLeche,  # primero los que toman leche
            -g.edad,          # edad descendente
            g.nombre          # nombre ascendente
        ))

    def mostrar(self):
        print(f"\nCentro Veterinario: {self.nombre}")

        print("\nPerros:")
        for p in self.perros:
            p.mostrar()

        print("\nGatos:")
        for g in self.gatos:
            g.mostrar()

    # d. Verificar dueños repetidos
    def verificar_duenos(self):
        contador = {}

        for p in self.perros:
            contador[p.nombreDueno] = contador.get(p.nombreDueno, 0) + 1

        for g in self.gatos:
            contador[g.nombreDueno] = contador.get(g.nombreDueno, 0) + 1

        for dueno, cantidad in contador.items():
            if cantidad >= 2:
                print(f"El dueño {dueno} tiene {cantidad} animales")


# a. Crear 2 centros con mínimo 2 perros y 2 gatos
cv1 = CentroVeterinario("Vet1")
cv2 = CentroVeterinario("Vet2")

# Centro 1
cv1.agregar_perro(Perro("Firulais", 5, "Juan", True, True))
cv1.agregar_perro(Perro("Rex", 3, "Ana", False, True))

cv1.agregar_gato(Gato("Michi", 2, "Juan", True, True))
cv1.agregar_gato(Gato("Pelusa", 4, "Luis", False, False))

# Centro 2
cv2.agregar_perro(Perro("Max", 2, "Carlos", True, False))
cv2.agregar_perro(Perro("Rocky", 2, "Carlos", False, True))

cv2.agregar_gato(Gato("Luna", 1, "Maria", True, True))
cv2.agregar_gato(Gato("Sol", 3, "Maria", False, False))

# b. Ordenar perros
cv1.ordenar_perros()
cv2.ordenar_perros()

# c. Ordenar gatos
cv1.ordenar_gatos()
cv2.ordenar_gatos()

# Mostrar
cv1.mostrar()
cv2.mostrar()

# d. Verificar dueños
print("\nDueños con más de un animal en Vet1:")
cv1.verificar_duenos()

print("\nDueños con más de un animal en Vet2:")
cv2.verificar_duenos()