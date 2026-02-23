# ============================================
# OPERADORES AUMENTADOS EN PYTHON ⚡
# ============================================

# Un operador aumentado hace la operación Y guarda el resultado
# en la misma variable. Es un atajo:
# x += 5  es igual a escribir  x = x + 5

# Pedimos un número base y uno para operar
x = eval(input("Ingresa el número base: "))
n = eval(input("Ingresa el número para operar: "))

print("============================")
print("Valor inicial de x:", x)
print("============================")

# SUMA ASIGNACIÓN
x += n
print(f"x += {n}  →  x ahora vale:", x)

# Reiniciamos x para ver cada operación por separado
x = eval(input("\nReinicia x: "))

# RESTA ASIGNACIÓN
x -= n
print(f"x -= {n}  →  x ahora vale:", x)

x = eval(input("Reinicia x: "))

# PRODUCTO ASIGNACIÓN
x *= n
print(f"x *= {n}  →  x ahora vale:", x)

x = eval(input("Reinicia x: "))

# POTENCIA ASIGNACIÓN
x **= n
print(f"x **= {n}  →  x ahora vale:", x)

x = eval(input("Reinicia x: "))

# DIVISIÓN REAL ASIGNACIÓN
x /= n
print(f"x /= {n}  →  x ahora vale:", x)

x = eval(input("Reinicia x: "))

# DIVISIÓN ENTERA ASIGNACIÓN
x //= n
print(f"x //= {n}  →  x ahora vale:", x)

x = eval(input("Reinicia x: "))

# RESTO ASIGNACIÓN
x %= n
print(f"x %= {n}  →  x ahora vale:", x)

print("============================")
