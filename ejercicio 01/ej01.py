class televisor:
    def __init__(self,marca,resolucion,tipo):
        self.marca = marca
        self.resolucion = resolucion
        self.tipo = tipo
    
    def __str__(self):
        return f"Marca: {self.marca}\nResolución: {self.resolucion}\nTipo: {self.tipo}"

if __name__ == "__main__":
    televisor1 = televisor("Samsung", "4K", "LED")
    televisor2 = televisor("LG", "Full HD", "OLED")
    print(televisor1)    
    print("---------------")
    print(televisor2)