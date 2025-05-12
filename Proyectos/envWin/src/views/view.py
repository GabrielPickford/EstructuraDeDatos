import tkinter as tk
from tkinter import font


class View:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Bitwise")
        master.configure(bg="#2b2b2b")

        # Fuente personalizada
        self.custom_font = font.Font(family="Helvetica", size=11)
        self.title_font = font.Font(family="Helvetica", size=14, weight="bold")

        # Frame principal
        self.main_frame = tk.Frame(master, bg="#2b2b2b", padx=20, pady=20)
        self.main_frame.pack()

        # Título
        self.title_label = tk.Label(
            self.main_frame,
            text="Calculadora Bitwise",
            font=self.title_font,
            bg="#2b2b2b",
            fg="#f0f0f0",
        )
        self.title_label.pack(pady=(0, 10))

        # Entradas
        self.label1 = tk.Label(
            self.main_frame,
            text="Primer número entero:",
            font=self.custom_font,
            bg="#2b2b2b",
            fg="#f0f0f0",
        )
        self.label1.pack(anchor="w")
        self.entry1 = tk.Entry(self.main_frame, bg="#1e1e1e", fg="#f0f0f0", width=30)
        self.entry1.pack(pady=(0, 10))

        self.label2 = tk.Label(
            self.main_frame,
            text="Segundo número entero (para AND, OR, XOR):",
            font=self.custom_font,
            bg="#2b2b2b",
            fg="#f0f0f0",
        )
        self.label2.pack(anchor="w")
        self.entry2 = tk.Entry(self.main_frame, bg="#1e1e1e", fg="#f0f0f0", width=30)
        self.entry2.pack(pady=(0, 10))

        self.label3 = tk.Label(
            self.main_frame,
            text="Número entero (para NOT, Shift):",
            font=self.custom_font,
            bg="#2b2b2b",
            fg="#f0f0f0",
        )
        self.label3.pack(anchor="w")
        self.entry3 = tk.Entry(self.main_frame, bg="#1e1e1e", fg="#f0f0f0", width=30)
        self.entry3.pack(pady=(0, 20))

        # Resultado
        self.result_label = tk.Label(
            self.main_frame,
            text="Result:",
            font=self.custom_font,
            bg="#2b2b2b",
            fg="#f0f0f0",
        )
        self.result_label.pack(anchor="w")
        self.result_display = tk.Text(
            self.main_frame,
            height=5,
            width=40,
            bg="#1e1e1e",
            fg="#f0f0f0",
            insertbackground="#ffffff",
        )
        self.result_display.pack(pady=(0, 20))

        # Botones
        self.button_frame = tk.Frame(self.main_frame, bg="#2b2b2b")
        self.button_frame.pack()

        self.and_button = tk.Button(
            self.button_frame,
            text="AND",
            width=12,
            bg="#4caf50",
            fg="white",
            font=self.custom_font,
        )
        self.and_button.grid(row=0, column=0, padx=5, pady=5)

        self.or_button = tk.Button(
            self.button_frame,
            text="OR",
            width=12,
            bg="#2196f3",
            fg="white",
            font=self.custom_font,
        )
        self.or_button.grid(row=0, column=1, padx=5, pady=5)

        self.xor_button = tk.Button(
            self.button_frame,
            text="XOR",
            width=12,
            bg="#ff9800",
            fg="white",
            font=self.custom_font,
        )
        self.xor_button.grid(row=0, column=2, padx=5, pady=5)

        self.not_button = tk.Button(
            self.button_frame,
            text="NOT",
            width=12,
            bg="#9c27b0",
            fg="white",
            font=self.custom_font,
        )
        self.not_button.grid(row=1, column=0, padx=5, pady=5)

        self.left_shift_button = tk.Button(
            self.button_frame,
            text="Left Shift",
            width=12,
            bg="#607d8b",
            fg="white",
            font=self.custom_font,
        )
        self.left_shift_button.grid(row=1, column=1, padx=5, pady=5)

        self.right_shift_button = tk.Button(
            self.button_frame,
            text="Right Shift",
            width=12,
            bg="#f44336",
            fg="white",
            font=self.custom_font,
        )
        self.right_shift_button.grid(row=1, column=2, padx=5, pady=5)

    def get_input_values(self):
        num1 = self.entry1.get()
        num2 = self.entry2.get()
        num3 = self.entry3.get()
        return num1, num2, num3

    def clear_result(self):
        self.result_display.delete(1.0, tk.END)

    def display_result(self, result):
        self.clear_result()
        self.result_display.insert(tk.END, f"Decimal: {result['decimal']}\n")
        self.result_display.insert(tk.END, f"Binary: {result['binary']}\n")

    def bind_and_button(self, callback):
        self.and_button.config(command=callback)

    def bind_or_button(self, callback):
        self.or_button.config(command=callback)

    def bind_xor_button(self, callback):
        self.xor_button.config(command=callback)

    def bind_not_button(self, callback):
        self.not_button.config(command=callback)

    def bind_left_shift_button(self, callback):
        self.left_shift_button.config(command=callback)

    def bind_right_shift_button(self, callback):
        self.right_shift_button.config(command=callback)
