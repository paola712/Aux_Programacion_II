class Libro:
    def __init__(self, nombre, autor, anio):
        self.nombre = nombre
        self.autor = autor
        self.anio = anio

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Autor: {self.autor}, Año: {self.anio}")


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.cantLibros = 0

    def agregar_libro(self, libro):
        if self.cantLibros < 100:
            self.libros.append(libro)
            self.cantLibros += 1
        else:
            print("No se pueden agregar más libros")

    def buscar_libro(self, nombre):
        for libro in self.libros:
            if libro.nombre == nombre:
                print(f"Libro encontrado en {self.nombre}:")
                libro.mostrar()
                return True
        print(f"Libro '{nombre}' no encontrado en {self.nombre}")
        return False

    def mostrar(self):
        print(f"\nBiblioteca: {self.nombre}")
        print(f"Cantidad de libros: {self.cantLibros}")
        for libro in self.libros:
            libro.mostrar()


# b. Instanciar 2 bibliotecas y agregar libros
b1 = Biblioteca("Central")
b2 = Biblioteca("Zona Sur")

b1.agregar_libro(Libro("Python", "Guido", 1991))
b1.agregar_libro(Libro("Java", "James", 1995))

b2.agregar_libro(Libro("C++", "Bjarne", 1985))
b2.agregar_libro(Libro("Rust", "Graydon", 2010))

# c. Buscar libro
b1.buscar_libro("Python")
b2.buscar_libro("Python")

# d. Mostrar biblioteca con más libros
print("\nBiblioteca(s) con más libros:")
if b1.cantLibros > b2.cantLibros:
    b1.mostrar()
elif b2.cantLibros > b1.cantLibros:
    b2.mostrar()
else:
    b1.mostrar()
    b2.mostrar()