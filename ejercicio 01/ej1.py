class anime:
    def __init__(self, nombre, genero, nro_episodios):
        self.nombre = nombre
        self.genero = genero
        self.nro_episodios = nro_episodios
        self.episodios = []

    def __str__(self):
        return f"Nombre: {self.nombre}\nGenero: {self.genero}\nNúmero de episodios: {self.nro_episodios}\nEpisodios: {len(self.episodios)}"
    
if __name__ == "__main__":
    anime1 = anime("Naruto", "Shonen", 220)
    anime2 = anime("One Piece", "Shonen", 1000)
    anime1.episodios.append("Episodio 1: Naruto Uzumaki")
    anime2.episodios.append("Episodio 1: Luffy y el sombrero de paja")
    print(anime1)
    print("---------------")
    print(anime2)