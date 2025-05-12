class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        # Vincula los botones con las funciones correspondientes
        self.view.bind_and_button(self.perform_and)
        self.view.bind_or_button(self.perform_or)
        self.view.bind_xor_button(self.perform_xor)
        self.view.bind_not_button(self.perform_not)
        self.view.bind_left_shift_button(self.perform_left_shift)
        self.view.bind_right_shift_button(self.perform_right_shift)

    def perform_and(self):
        try:
            num1, num2, _ = self.view.get_input_values()
            num1, num2 = int(num1), int(num2)
            result = self.model.bitwise_and(num1, num2)
            self.view.display_result(result)
        except ValueError:
            self.view.display_result({"decimal": "Error", "binary": "Invalid input"})

    def perform_or(self):
        try:
            num1, num2, _ = self.view.get_input_values()
            num1, num2 = int(num1), int(num2)
            result = self.model.bitwise_or(num1, num2)
            self.view.display_result(result)
        except ValueError:
            self.view.display_result({"decimal": "Error", "binary": "Invalid input"})

    def perform_xor(self):
        try:
            num1, num2, _ = self.view.get_input_values()
            num1, num2 = int(num1), int(num2)
            result = self.model.bitwise_xor(num1, num2)
            self.view.display_result(result)
        except ValueError:
            self.view.display_result({"decimal": "Error", "binary": "Invalid input"})

    def perform_not(self):
        try:
            _, _, num3 = self.view.get_input_values()
            num3 = int(num3)
            result = self.model.bitwise_not(num3)
            self.view.display_result(result)
        except ValueError:
            self.view.display_result({"decimal": "Error", "binary": "Invalid input"})

    def perform_left_shift(self):
        try:
            _, _, num3 = self.view.get_input_values()
            num3, shift = map(int, num3.split(","))
            result = self.model.left_shift(num3, shift)
            self.view.display_result(result)
        except (ValueError, IndexError):
            self.view.display_result({"decimal": "Error", "binary": "Invalid input"})

    def perform_right_shift(self):
        try:
            _, _, num3 = self.view.get_input_values()
            num3, shift = map(int, num3.split(","))
            result = self.model.right_shift(num3, shift)
            self.view.display_result(result)
        except (ValueError, IndexError):
            self.view.display_result({"decimal": "Error", "binary": "Invalid input"})
