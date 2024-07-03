from mean_var_std import calculate

# Ejemplo de prueba
print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

# Ejemplo de prueba con lista incorrecta
try:
    print(calculate([0, 1, 2]))
except ValueError as e:
    print(e)
