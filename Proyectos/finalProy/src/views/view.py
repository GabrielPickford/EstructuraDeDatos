# views/view.py
import tkinter as tk
from tkinter import font


class View:
    def __init__(self, master):
        self.master = master
        master.title("Validador de Paréntesis y Símbolos")
        master.configure(bg="#2b2b2b")

        # Fuente personalizada
        self.custom_font = font.Font(family="Helvetica", size=11)
        self.title_font = font.Font(family="Helvetica", size=14, weight="bold")

        # Frame principal
        self.main_frame = tk.Frame(master, bg="#2b2b2b", padx=20, pady=20)
        self.main_frame.pack(anchor="center", expand=True)

        # Título
        self.title_label = tk.Label(
            self.main_frame,
            text="Validador de Paréntesis y Símbolos",
            font=self.title_font,
            bg="#2b2b2b",
            fg="#f0f0f0",
        )
        self.title_label.pack(pady=(0, 10))

        # Entrada de texto
        self.expression_label = tk.Label(
            self.main_frame,
            text="Ingresa la expresión a validar:",
            font=self.custom_font,
            bg="#2b2b2b",
            fg="#f0f0f0",
        )
        self.expression_label.pack(anchor="center")

        self.expression_entry = tk.Entry(
            self.main_frame, bg="#1e1e1e", fg="#f0f0f0", width=40
        )
        self.expression_entry.pack(pady=(0, 10))

        # Resultado
        self.result_label = tk.Label(
            self.main_frame,
            text="Resultado:",
            font=self.custom_font,
            bg="#2b2b2b",
            fg="#f0f0f0",
        )
        self.result_label.pack(anchor="center")

        self.result_display = tk.Text(
            self.main_frame,
            height=5,
            width=40,
            bg="#1e1e1e",
            fg="#f0f0f0",
            insertbackground="#ffffff",
            wrap=tk.WORD,
        )
        self.result_display.pack(pady=(0, 20))

        # Botón de validación
        self.validate_button = tk.Button(
            self.main_frame,
            text="Validar Expresión",
            width=20,
            bg="#4caf50",
            fg="white",
            font=self.custom_font,
        )
        self.validate_button.pack(pady=(0, 10))

    def get_expression(self):
        """Obtiene la expresión ingresada por el usuario"""
        return self.expression_entry.get()

    def clear_result(self):
        """Limpia el área de resultado"""
        self.result_display.delete(1.0, tk.END)

    def display_result(self, result):
        """Muestra el resultado de la validación"""
        self.clear_result()
        if result["valid"]:
            self.result_display.insert(
                tk.END, f"¡La expresión es válida! \n{result['message']}"
            )
        else:
            self.result_display.insert(tk.END, f"Error: \n{result['message']}")

    def bind_validate_button(self, callback):
        """Vincula el evento del botón de validación"""
        self.validate_button.config(command=callback)
