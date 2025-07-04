# Recurrencia del problema del ladrón
# -----------------------------------
#    t(n) = max (t(n-2) + v[n], t(n-1))
#    t(n) = 0		               : si n<0

def solve_tabulation(items):
    table = []

    def fill_table():
        # Rellena la tabla 'table' con las soluciones de todos los
        # subproblemas (o sea, los beneficios máximos que puede
        # conseguir el ladrón)
        # ...
        table.append(items[0])
        table.append(max(items[0], items[1]))
        for j in range(2, len(items)):
            table.append(max(table[j - 2] + items[j], table[j - 1]))
        return

    fill_table()

    max_benefit = table[-1]  # El máximo beneficio está en el
    # último elemento de la tabla
    return max_benefit
