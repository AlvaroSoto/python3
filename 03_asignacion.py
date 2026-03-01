# ============================================
# OPERADORES AUMENTADOS EN PYTHON ⚡
# ============================================

# Un operador aumentado hace la operación Y guarda el resultado
# en la misma variable. Es un atajo:
# x += 5  es igual a escribir  x = x + 5

# Pedimos un número base y uno para operar (float acepta enteros y decimales)
x_original = float(input("Ingresa el número base: "))
n          = float(input("Ingresa el número para operar: "))

print("============================")
print(f"Valor inicial de x: {x_original}")
print(f"Número a operar (n): {n}")
print("============================")

# En cada bloque:
#   1. Restauramos x a su valor original
#   2. Aplicamos el operador aumentado
#   3. Mostramos la operación equivalente y el resultado

# SUMA ASIGNACIÓN
x = x_original
x += n
print(f"x += {n}   →   {x_original} + {n} = {x}")

# RESTA ASIGNACIÓN
x = x_original
x -= n
print(f"x -= {n}   →   {x_original} - {n} = {x}")

# PRODUCTO ASIGNACIÓN
x = x_original
x *= n
print(f"x *= {n}   →   {x_original} * {n} = {x}")

# POTENCIA ASIGNACIÓN
x = x_original
x **= n
print(f"x **= {n}  →   {x_original} ** {n} = {x}")

# DIVISIÓN REAL ASIGNACIÓN
x = x_original
x /= n
print(f"x /= {n}   →   {x_original} / {n} = {x}")

# DIVISIÓN ENTERA ASIGNACIÓN
x = x_original
x //= n
print(f"x //= {n}  →   {x_original} // {n} = {x}")

# RESTO ASIGNACIÓN
x = x_original
x %= n
print(f"x %= {n}   →   {x_original} % {n} = {x}")

print("============================")
