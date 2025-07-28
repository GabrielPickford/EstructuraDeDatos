import tkinter as tk

from controllers.controller import Controller
from models.model import DataModel as Model
from views.view import View


def main():
    root = tk.Tk()
    root.geometry("500x500")
    view = View(root)

    model = Model()

    controller = Controller(view, model)

    root.mainloop()


if __name__ == "__main__":
    main()
