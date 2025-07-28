# models/model.py


class DataModel:
    def __init__(self):
        # La pila se implementa como una lista
        self.stack = []

    def is_matching_pair(self, opening, closing):
        """Verifica si los símbolos forman un par válido."""
        pairs = {"(": ")", "[": "]", "{": "}"}
        return pairs.get(opening) == closing

    def validate_expression(self, expresion):
        """
        Valida si una expresión tiene paréntesis, corchetes y llaves balanceadas.
        Retorna un diccionario con el resultado y mensaje.
        """
        self.stack = []
        for idx, char in enumerate(expresion):
            if char in "([{":
                self.stack.append(char)
            elif char in ")]}":
                if not self.stack:
                    return {
                        "valid": False,
                        "message": f"Error: símbolo de cierre '{char}' sin apertura en posición {idx}.",
                    }
                top = self.stack.pop()
                if not self.is_matching_pair(top, char):
                    return {
                        "valid": False,
                        "message": f"Error: símbolo '{char}' en posición {idx} no coincide con '{top}'.",
                    }

        if self.stack:
            return {
                "valid": False,
                "message": f"Error: símbolo(s) de apertura sin cerrar: {''.join(self.stack)}.",
            }

        return {"valid": True, "message": "La expresión está correctamente balanceada."}
