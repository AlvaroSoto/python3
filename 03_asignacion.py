# ============================================
# OPERADORES AUMENTADOS EN PYTHON
# ============================================

# Un operador aumentado hace la operación Y guarda el resultado
# en la misma variable. Es un atajo:
# x += 5  es igual a escribir  x = x + 5

x = float(input("Ingresa el número base: "))
n = float(input("Ingresa el número para operar: "))

print("============================")

antes = x
x += n
print(f"x += {n}    →   x era {antes},  ahora x = {x}")

x = antes
x -= n
print(f"x -= {n}    →   x era {antes},  ahora x = {x}")

x = antes
x *= n
print(f"x *= {n}    →   x era {antes},  ahora x = {x}")

x = antes
x **= n
print(f"x **= {n}   →   x era {antes},  ahora x = {x}")

x = antes
x /= n
print(f"x /= {n}    →   x era {antes},  ahora x = {x}")

x = antes
x //= n
print(f"x //= {n}   →   x era {antes},  ahora x = {x}")

x = antes
x %= n
print(f"x %= {n}    →   x era {antes},  ahora x = {x}")

print("============================")
