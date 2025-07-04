# 1. Copia aqui tu solución del primer ejercicio de esta semana

def next_number(digits, base):
    next_digits = digits.copy()

    # Añade tu código aqui
    # ...

    for i in range(len(digits) - 1, -1, -1):
        if (i == len(digits) - 1):
            next_digits[i] = digits[i] + 1
        if (next_digits[i] > base - 1):
            next_digits[i] = 0
            if (i > 0):
                next_digits[i - 1] = next_digits[i - 1] + 1
    return next_digits


# ----------------------------------------------------------

class My_Iterator:

    def __init__(self, num_digits, base):
        # 2.1 Añade código aqui
        # ...
        self.base = base
        self.num_digits = num_digits

    def next(self):
        # 2.2 Añade código aqui
        # ...
        digits = [0] * self.num_digits
        digits[len(digits)-1] = -1
        for i in range(self.base ** self.num_digits):
            digits = next_number(digits, self.base)
            yield digits

        # Cuando no quedan valores simplemente retornamos
        return
