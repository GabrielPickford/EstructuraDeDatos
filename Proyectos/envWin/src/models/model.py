class DataModel:
    def __init__(self):
        self.result = None

    def _formatear_binario(self, num):
        bin_str = bin(num)[2:]  # elimina '0b'
        if len(bin_str) < 16:
            bin_str = bin_str.zfill(16)  # rellena con ceros a la izquierda

        # Agrupa en bloques de 4 bits desde la derecha
        grupos = []
        while bin_str:
            grupos.insert(0, bin_str[-4:])  # toma los últimos 4 bits
            bin_str = bin_str[:-4]  # elimina esos bits del final
        return "_".join(grupos)

    def bitwise_and(self, num1, num2):
        result_decimal = num1 & num2
        result_binary = self._formatear_binario(result_decimal)
        return {"decimal": result_decimal, "binary": result_binary}

    def bitwise_or(self, num1, num2):
        result_decimal = num1 | num2
        result_binary = self._formatear_binario(result_decimal)
        return {"decimal": result_decimal, "binary": result_binary}

    def bitwise_xor(self, num1, num2):
        result_decimal = num1 ^ num2
        result_binary = self._formatear_binario(result_decimal)
        return {"decimal": result_decimal, "binary": result_binary}

    def bitwise_not(self, num1):
        result_decimal = ~num1
        result_binary = self._formatear_binario(result_decimal & 0xFFFF)
        return {"decimal": result_decimal, "binary": result_binary}

    def left_shift(self, num1, shift):
        result_decimal = num1 << shift
        result_binary = self._formatear_binario(result_decimal)
        return {"decimal": result_decimal, "binary": result_binary}

    def right_shift(self, num1, shift):
        result_decimal = num1 >> shift
        result_binary = self._formatear_binario(result_decimal)
        return {"decimal": result_decimal, "binary": result_binary}
