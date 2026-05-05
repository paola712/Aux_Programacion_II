class Cancion:
    def __init__(self, titulo, artista):
        self.__titulo = titulo
        self.__artista = artista

    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista

    def __str__(self):
        return f"Cancion[ {self.__titulo} - {self.__artista} ]"


class Playlist:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__canciones = []

    def agregarCancion(self, cancion):
        self.__canciones.append(cancion)

    def eliminarCancion(self, cancion):
        if cancion in self.__canciones:
            self.__canciones.remove(cancion)

    def getCanciones(self):
        return self.__canciones

    def __str__(self):
        lista = ""
        for c in self.__canciones:
            lista += str(c) + "\n"
        return f"Playlist: {self.__nombre}\n{lista}"


# ===== MAIN =====
print("Crear canciones.")
c1 = Cancion("Song A", "Artista 1")
c2 = Cancion("Song B", "Artista 2")
c3 = Cancion("Song C", "Artista 3")

print("\nCrear playlist.")
p = Playlist("Mis favoritas")

p.agregarCancion(c1)
p.agregarCancion(c2)
p.agregarCancion(c3)

print("\nPlaylist actual:")
print(p)

print("Eliminar una canción.")
p.eliminarCancion(c2)

print("\nPlaylist actualizada:")
print(p)

print("Eliminar playlist.")
del p

print("\nLas canciones siguen existiendo:")
print(c1)
print(c2)
print(c3)