class Aula:
    def __init__(self, nombre_aula, piso):
        self.nombre_aula = nombre_aula
        self.piso = piso
        self.estudiantes = {
            "Luis": 67,
            "Aracely": 89
        }

    def mostrar(self, opcion=None):

        if opcion is None:
            print("Nombre del aula:", self.nombre_aula)
            print("Piso:", self.piso)
            print("Estudiantes y notas:")
            for nombre, nota in self.estudiantes.items():
                print(nombre, "-", nota)

        else:
            print("Resultados:")
            for nombre, nota in self.estudiantes.items():
                if nota >= 51:
                    estado = "APROBADO"
                else:
                    estado = "REPROBADO"
                print(nombre, "-", nota, "-", estado)

aula1 = Aula("Aula A1", 2)

aula1.mostrar()

print()

aula1.mostrar(1)