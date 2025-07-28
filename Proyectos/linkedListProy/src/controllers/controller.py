from tkinter import messagebox

from models.model import Biblioteca, PlaylistCollection


class Controller:
    def __init__(self, view, model):
        """Inicializa la vista y el modelo."""
        self.view = view
        self.biblioteca = model  # Instancia de Biblioteca
        self.playlists = PlaylistCollection()  # Manejar múltiples playlists

        # Vinculamos los botones de la vista a los métodos del controlador
        self.view.bind_add_button(self.add_song)
        self.view.bind_search_button(self.search_song)
        self.view.bind_delete_button(self.delete_song)
        self.view.bind_show_button(self.show_library)
        self.view.bind_create_playlist_button(self.create_playlist)
        self.view.bind_show_playlists_button(self.show_all_playlists)
        self.view.bind_add_song_to_playlist_button(
            self.add_song_to_playlist
        )  # CORREGIDO

    def add_song(self):
        """Añadir una canción a la biblioteca."""
        titulo, artista, album = self.view.get_input_values()

        if titulo and artista and album:
            self.biblioteca.añadir_cancion(titulo, artista, album)
            self.view.display_message(f"¡Canción '{titulo}' añadida correctamente!")
        else:
            self.view.display_message("Por favor, complete todos los campos.")

    def search_song(self):
        """Buscar una canción en la biblioteca."""
        busqueda = self.view.entry_titulo.get()  # Buscamos por título o artista
        if busqueda:
            result = self.biblioteca.buscar_cancion(busqueda)
            if result:
                self.view.display_result([result])  # Mostrar solo la canción encontrada
            else:
                self.view.display_message(
                    "No se encontró ninguna canción con ese título o artista."
                )
        else:
            self.view.display_message(
                "Por favor, ingrese el título o el artista para buscar."
            )

    def delete_song(self):
        """Eliminar una canción de la biblioteca."""
        titulo = self.view.entry_titulo.get()  # Usamos el título para eliminar
        if titulo:
            if self.biblioteca.eliminar_cancion(titulo):
                self.view.display_message(
                    f"Canción '{titulo}' eliminada correctamente."
                )
            else:
                self.view.display_message(
                    f"No se encontró la canción '{titulo}' para eliminar."
                )
        else:
            self.view.display_message(
                "Por favor, ingrese el título de la canción que desea eliminar."
            )

    def show_library(self):
        """Mostrar todas las canciones de la biblioteca."""
        self.view.clear_results()
        if self.biblioteca.cabeza is None:
            self.view.display_message("La biblioteca está vacía.")
        else:
            canciones = []
            actual = self.biblioteca.cabeza
            while actual:
                canciones.append(actual.datos)
                actual = actual.siguiente
            self.view.display_result(canciones)

    def create_playlist(self):
        """Crear una nueva playlist."""
        nombre_playlist = self.view.entry_titulo.get()
        if nombre_playlist:
            self.playlists.crear_playlist(nombre_playlist)
            self.view.display_message(
                f"Playlist '{nombre_playlist}' creada correctamente."
            )
        else:
            self.view.display_message("Por favor, ingrese un nombre para la playlist.")

    def show_all_playlists(self):
        """Mostrar todas las playlists existentes."""
        self.view.clear_results()
        if not self.playlists.playlists:
            self.view.display_message("No hay playlists disponibles.")
        else:
            for playlist in self.playlists.playlists.values():
                canciones = []
                actual = playlist.cabeza
                while actual:
                    canciones.append(actual.datos)
                    actual = actual.siguiente
                self.view.display_result(
                    canciones, titulo=f"Playlist: {playlist.nombre}"
                )

    def add_song_to_playlist(self):
        """Añadir una canción de la biblioteca a una playlist existente."""
        nombre_playlist = self.view.entry_playlist.get()  # Input del nombre de playlist
        titulo_cancion = self.view.entry_titulo.get()  # Input del título de la canción

        if not nombre_playlist:
            self.view.display_message("Por favor, ingrese el nombre de la playlist.")
            return
        if not titulo_cancion:
            self.view.display_message("Por favor, ingrese el título de la canción.")
            return

        # Buscar la canción en la biblioteca
        cancion = self.biblioteca.buscar_cancion(titulo_cancion)
        if cancion is None:
            self.view.display_message(
                f"No se encontró la canción '{titulo_cancion}' en la biblioteca."
            )
            return

        # Añadir la canción a la playlist
        if nombre_playlist not in self.playlists.playlists:
            self.view.display_message(f"La playlist '{nombre_playlist}' no existe.")
            return

        self.playlists.playlists[nombre_playlist].añadir_cancion(cancion)
        self.view.display_message(
            f"Canción '{titulo_cancion}' añadida a la playlist '{nombre_playlist}'."
        )
