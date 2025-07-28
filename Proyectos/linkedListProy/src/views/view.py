import tkinter as tk
from tkinter import ttk  # Usamos ttk para el scrollbar
from tkinter import font, messagebox


class View:
    def __init__(self, master):
        self.master = master
        master.title("Biblioteca Musical")
        master.configure(bg="black")  # Fondo
        master.geometry("1200x600")  # Tamaño

        # Fuente personalizada
        self.custom_font = font.Font(family="Helvetica", size=12)
        self.title_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.subtitle_font = font.Font(family="Helvetica", size=14, weight="bold")
        self.song_title_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.artist_font = font.Font(family="Helvetica", size=14, weight="normal")

        # Frame principal
        self.main_frame = tk.Frame(master, bg="black")
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # Configuración de las columnas (1/4 izquierda, 3/4 derecha)
        self.main_frame.grid_columnconfigure(0, weight=1, minsize=250)  # 1/4
        self.main_frame.grid_columnconfigure(1, weight=3, minsize=750)  # 3/4

        # Título
        self.title_label = tk.Label(
            self.main_frame,
            text="Biblioteca Musical",
            font=self.title_font,
            bg="black",  # Fondo negro
            fg="#1db954",  # Verde Spotify
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Frame para Inputs y Botones (Lado izquierdo)
        self.inputs_frame = tk.Frame(self.main_frame, bg="#282828")  # Gris oscuro
        self.inputs_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 20))

        # Entradas
        self.label1 = tk.Label(
            self.inputs_frame,
            text="Título:",
            font=self.subtitle_font,
            bg="#282828",  # Gris oscuro
            fg="#ffffff",
        )
        self.label1.grid(
            row=0,
            column=0,
            pady=(0, 10),
            sticky="w",
        )
        self.entry_titulo = tk.Entry(
            self.inputs_frame,
            bg="#383838",  # Gris intermedio para entradas
            fg="#ffffff",
            width=35,
            bd=0,
            highlightthickness=0,
        )
        self.entry_titulo.grid(row=1, column=0, pady=(0, 10))

        self.label2 = tk.Label(
            self.inputs_frame,
            text="Artista:",
            font=self.subtitle_font,
            bg="#282828",  # Gris oscuro
            fg="#ffffff",
        )
        self.label2.grid(row=2, column=0, pady=(0, 10), sticky="w")
        self.entry_artista = tk.Entry(
            self.inputs_frame,
            bg="#383838",  # Gris intermedio para entradas
            fg="#ffffff",
            width=35,
            bd=0,
            highlightthickness=0,
        )
        self.entry_artista.grid(row=3, column=0, pady=(0, 10))

        self.label3 = tk.Label(
            self.inputs_frame,
            text="Álbum:",
            font=self.subtitle_font,
            bg="#282828",  # Gris oscuro
            fg="#ffffff",
        )
        self.label3.grid(row=4, column=0, pady=(0, 10), sticky="w")
        self.entry_album = tk.Entry(
            self.inputs_frame,
            bg="#383838",  # Gris intermedio para entradas
            fg="#ffffff",
            width=35,
            bd=0,
            highlightthickness=0,
        )
        self.entry_album.grid(row=5, column=0, pady=(0, 20))

        self.label_playlist = tk.Label(
            self.inputs_frame,
            text="Nombre Playlist:",
            font=self.subtitle_font,
            bg="#282828",
            fg="#ffffff",
        )
        self.label_playlist.grid(row=6, column=0, pady=(0, 10), sticky="w")
        self.entry_playlist = tk.Entry(
            self.inputs_frame,
            bg="#383838",
            fg="#ffffff",
            width=35,
            bd=0,
            highlightthickness=0,
        )
        self.entry_playlist.grid(row=7, column=0, pady=(0, 20))

        # Botones
        self.button_frame = tk.Frame(self.inputs_frame, bg="#282828")  # Gris oscuro
        self.button_frame.grid(row=8, column=0, pady=10)

        self.add_button = tk.Button(
            self.button_frame,
            text="Añadir Canción",
            width=20,
            bg="#1db954",
            fg="white",
            font=self.custom_font,
            relief="flat",
            bd=0,
            activebackground="#1ed760",
        )
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.search_button = tk.Button(
            self.button_frame,
            text="Buscar Canción",
            width=20,
            bg="#1db954",
            fg="white",
            font=self.custom_font,
            relief="flat",
            bd=0,
            activebackground="#1ed760",
        )
        self.search_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = tk.Button(
            self.button_frame,
            text="Eliminar Canción",
            width=20,
            bg="#ff5f57",  # Color rojo para eliminar
            fg="white",
            font=self.custom_font,
            relief="flat",
            bd=0,
            activebackground="#ff2e2e",
        )
        self.delete_button.grid(row=1, column=0, padx=5, pady=5)

        self.show_button = tk.Button(
            self.button_frame,
            text="Mostrar Biblioteca",
            width=20,
            bg="#007b7f",
            fg="white",
            font=self.custom_font,
            relief="flat",
            bd=0,
            activebackground="#009999",
        )
        self.show_button.grid(row=1, column=1, padx=5, pady=5)

        self.create_playlist_button = tk.Button(
            self.button_frame,
            text="Crear Playlist",
            width=20,
            bg="#ff9600",
            fg="white",
            font=self.custom_font,
            relief="flat",
            bd=0,
            activebackground="#ff6700",  # Color activo
        )
        self.create_playlist_button.grid(row=2, column=0, padx=5, pady=5)

        self.show_playlists_button = tk.Button(
            self.button_frame,
            text="Mostrar Playlists",
            width=20,
            bg="#008080",  # Verde azulado
            fg="white",
            font=self.custom_font,
            relief="flat",
            bd=0,
            activebackground="#00cccc",
        )
        self.show_playlists_button.grid(row=2, column=1, padx=5, pady=5)

        self.add_song_to_playlist_button = tk.Button(
            self.button_frame,
            text="Añadir a Playlist",
            width=20,
            bg="#ff9600",
            fg="white",
            font=self.custom_font,
            relief="flat",
            bd=0,
            activebackground="#ff6700",
        )
        self.add_song_to_playlist_button.grid(row=3, column=0, padx=5, pady=5)

        # Frame para los resultados con scroll
        self.results_frame = tk.Frame(self.main_frame, bg="#282828")  # Gris oscuro
        self.results_frame.grid(row=1, column=1, sticky="nsew")

        # Configuramos la expansión de las filas y columnas
        self.results_frame.grid_rowconfigure(0, weight=1)
        self.results_frame.grid_columnconfigure(0, weight=1)

        # Canvas para los resultados
        self.canvas = tk.Canvas(
            self.results_frame, bg="#282828", bd=0, highlightthickness=0
        )
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Scrollbar (usando ttk)
        self.scrollbar = ttk.Scrollbar(
            self.results_frame,
            orient="vertical",
            command=self.canvas.yview,
        )
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Frame para los elementos dentro del Canvas
        self.results_container = tk.Frame(self.canvas, bg="#282828")
        self.canvas.create_window((0, 0), window=self.results_container, anchor="nw")

        # Actualizar la región de visualización del canvas
        self.results_container.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    # Métodos para interactuar con el controlador

    def get_input_values(self):
        """Obtenemos los valores de entrada para la canción."""
        titulo = self.entry_titulo.get()
        artista = self.entry_artista.get()
        album = self.entry_album.get()
        return titulo, artista, album

    def clear_results(self):
        """Limpiar el área de resultados."""
        for widget in self.results_container.winfo_children():
            widget.destroy()

    def display_result(self, result, titulo=None):
        """Mostrar canciones, con un título opcional (por ejemplo, el nombre de la playlist)."""
        self.clear_results()

        if titulo:
            titulo_label = tk.Label(
                self.results_container,
                text=titulo,
                font=self.title_font,
                fg="#1db954",
                bg="#282828",
                pady=10,
            )
            titulo_label.pack(anchor="w", padx=10)

        if result:
            for song in result:
                song_frame = tk.Frame(self.results_container, bg="#282828", pady=10)
                song_frame.pack(fill="x", padx=10)

                title_label = tk.Label(
                    song_frame,
                    text=song["titulo"],
                    font=self.song_title_font,
                    fg="#ffffff",
                    bg="#282828",
                )
                title_label.pack(anchor="w")

                artist_label = tk.Label(
                    song_frame,
                    text=song["artista"],
                    font=self.artist_font,
                    fg="#bbbbbb",
                    bg="#282828",
                )
                artist_label.pack(anchor="w")

                album_label = tk.Label(
                    song_frame,
                    text=song["album"],
                    font=self.artist_font,
                    fg="#666666",
                    bg="#282828",
                )
                album_label.pack(anchor="w")
        else:
            self.display_message("No hay resultados para mostrar.")

    def display_message(self, message):
        """Mostrar mensajes en ventana emergente."""
        messagebox.showinfo("Información", message)

    # Métodos bind para que el controlador pueda conectar acciones

    def bind_add_button(self, callback):
        self.add_button.config(command=callback)

    def bind_search_button(self, callback):
        self.search_button.config(command=callback)

    def bind_delete_button(self, callback):
        self.delete_button.config(command=callback)

    def bind_show_button(self, callback):
        self.show_button.config(command=callback)

    def bind_create_playlist_button(self, callback):
        self.create_playlist_button.config(command=callback)

    def bind_show_playlists_button(self, callback):
        self.show_playlists_button.config(command=callback)

    def bind_add_song_to_playlist_button(self, callback):
        self.add_song_to_playlist_button.config(command=callback)
