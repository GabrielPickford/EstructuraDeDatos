class DataModel:
    def __init__(self):
        self.result = None

    def bitwise_and(self, num1, num2):
        result_decimal = num1 & num2
        result_binary = bin(result_decimal)[
            2:
        ]  # Convierte a binario sin el prefijo '0b'
        return {"decimal": result_decimal, "binary": result_binary}

    def bitwise_or(self, num1, num2):
        result_decimal = num1 | num2
        result_binary = bin(result_decimal)[2:]
        return {"decimal": result_decimal, "binary": result_binary}

    def bitwise_xor(self, num1, num2):
        result_decimal = num1 ^ num2
        result_binary = bin(result_decimal)[2:]
        return {"decimal": result_decimal, "binary": result_binary}

    def bitwise_not(self, num1):
        result_decimal = ~num1
        result_binary = bin(result_decimal & 0xFFFFFFFF)[
            2:
        ]  # Asegura 32 bits para binario
        return {"decimal": result_decimal, "binary": result_binary}

    def left_shift(self, num1, shift):
        result_decimal = num1 << shift
        result_binary = bin(result_decimal)[2:]
        return {"decimal": result_decimal, "binary": result_binary}

    def right_shift(self, num1, shift):
        result_decimal = num1 >> shift
        result_binary = bin(result_decimal)[2:]
        return {"decimal": result_decimal, "binary": result_binary}
