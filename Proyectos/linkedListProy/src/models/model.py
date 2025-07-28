# Clase Cancion: Representa un nodo de la lista enlazada, que contiene los datos de una canción.
class Cancion:
    def __init__(self, titulo, artista, album):
        self.datos = {"titulo": titulo, "artista": artista, "album": album}
        self.siguiente = None  # Apunta al siguiente nodo (canción) en la lista


# Clase Biblioteca: Contiene una lista enlazada de canciones y permite realizar operaciones sobre ellas.
class Biblioteca:
    def __init__(self):
        self.cabeza = None  # La cabeza de la lista enlazada (el primer nodo)

    def añadir_cancion(self, titulo, artista, album):
        """Añadir una nueva canción a la biblioteca."""
        nueva_cancion = Cancion(titulo, artista, album)
        if not self.cabeza:
            self.cabeza = nueva_cancion
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_cancion

    def buscar_cancion(self, busqueda):
        """Buscar una canción por título o artista (ignora mayúsculas/minúsculas)."""
        actual = self.cabeza
        while actual:
            if (
                busqueda.lower() in actual.datos["titulo"].lower()
                or busqueda.lower() in actual.datos["artista"].lower()
            ):
                return actual.datos  # Retorna los datos de la canción encontrada
            actual = actual.siguiente
        return None  # Retorna None si no encuentra la canción

    def eliminar_cancion(self, titulo):
        """Eliminar una canción de la biblioteca por su título."""
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.datos["titulo"].lower() == titulo.lower():
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Canción eliminada
            anterior = actual
            actual = actual.siguiente
        return False  # Si no se encuentra la canción

    def mostrar_biblioteca(self):
        """Mostrar todas las canciones en la biblioteca."""
        actual = self.cabeza
        if not actual:
            print("La biblioteca está vacía.")
        else:
            while actual:
                print(
                    f"Título: {actual.datos['titulo']} | Artista: {actual.datos['artista']} | Álbum: {actual.datos['album']}"
                )
                actual = actual.siguiente


# Clase Playlist: Contiene una lista enlazada de canciones seleccionadas para una playlist.
class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la playlist
        self.cabeza = None  # La cabeza de la lista enlazada

    def añadir_cancion(self, cancion):
        """Añadir una canción a la playlist."""
        nueva_cancion = Cancion(cancion["titulo"], cancion["artista"], cancion["album"])
        if not self.cabeza:
            self.cabeza = nueva_cancion
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nueva_cancion

    def mostrar_playlist(self):
        """Mostrar todas las canciones de la playlist."""
        actual = self.cabeza
        if not actual:
            print(f"La playlist '{self.nombre}' está vacía.")
        else:
            print(f"Playlist: {self.nombre}")
            while actual:
                print(
                    f"Título: {actual.datos['titulo']} | Artista: {actual.datos['artista']} | Álbum: {actual.datos['album']}"
                )
                actual = actual.siguiente

    def obtener_canciones(self):
        """Devuelve todas las canciones de la playlist como una lista de diccionarios."""
        canciones = []
        actual = self.cabeza
        while actual:
            canciones.append(actual.datos)
            actual = actual.siguiente
        return canciones


# Clase PlaylistCollection: Maneja múltiples playlists
class PlaylistCollection:
    def __init__(self):
        self.playlists = {}  # Diccionario de playlists por nombre

    def crear_playlist(self, nombre):
        if nombre in self.playlists:
            print(f"La playlist '{nombre}' ya existe.")
        else:
            self.playlists[nombre] = Playlist(nombre)

    def obtener_playlist(self, nombre):
        return self.playlists.get(nombre)

    def añadir_cancion_a_playlist(self, nombre_playlist, cancion):
        """Añadir una canción (diccionario) a una playlist específica."""
        playlist = self.obtener_playlist(nombre_playlist)
        if playlist:
            playlist.añadir_cancion(cancion)
        else:
            print(f"No existe la playlist '{nombre_playlist}'.")

    def mostrar_todas(self):
        if not self.playlists:
            print("No hay playlists disponibles.")
        else:
            for playlist in self.playlists.values():
                playlist.mostrar_playlist()
                print("-" * 40)
