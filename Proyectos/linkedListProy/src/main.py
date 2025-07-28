import tkinter as tk

from controllers.controller import Controller
from models.model import Biblioteca  # Cambiar a Biblioteca
from views.view import View


def main():
    root = tk.Tk()
    root.geometry("500x500")
    view = View(root)

    model = Biblioteca()  # Instancia del modelo Biblioteca

    controller = Controller(view, model)  # Pasamos la vista y el modelo al controlador

    root.mainloop()


if __name__ == "__main__":
    main()
