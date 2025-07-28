# controllers/controller.py
from models.model import DataModel
from views.view import View


class Controller:
    def __init__(self, view: View, model: DataModel):
        self.view = view
        self.model = model

        # Vincula la acción del botón de validación
        self.view.bind_validate_button(self.validate_expression)

    def validate_expression(self):
        """Obtiene la expresión, la valida usando el modelo y muestra el resultado en la vista"""
        expresion = self.view.get_expression()

        if not expresion:  # Si no hay expresión
            self.view.display_result(
                {"valid": False, "message": "Por favor, ingresa una expresión."}
            )
            return

        # Llamar al modelo para validar la expresión
        result = self.model.validate_expression(expresion)

        # Mostrar el resultado en la vista
        self.view.display_result(result)
