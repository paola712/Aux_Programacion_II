class Instrumento:
    def __init__(self, nombre, material, tipo):
        self.nombre = nombre
        self.material = material
        self.tipo = tipo

    def __str__(self):
        return (f"Instrumento: {self.nombre}\n"
                f"Material: {self.material}\n"
                f"Tipo: {self.tipo}")
    def get_nombre(self):
        return self.nombre

    def get_material(self):
        return self.material

    def get_tipo(self):
        return self.tipo

   
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_material(self, material):
        self.material = material

    def set_tipo(self, tipo):
        self.tipo = tipo



if __name__ == "__main__":
    i1 = Instrumento("Guitarra", "Madera", "Cuerda y aire")
    i2 = Instrumento("Batería", "Metal y plástico", "Percusión")
    print(i1)
    print("---------------")
    print(i2)
    
    i1.set_nombre("Piano")
    i2.set_material("Madera y metal")

    print("---------------")
    print("Después de modificar:")
    print(i1)
    print("---------------")
    print(i2)