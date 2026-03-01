# ============================================
# OPERADORES AUMENTADOS EN PYTHON
# ============================================

# Un operador aumentado hace la operación Y guarda el resultado
# en la misma variable. Es un atajo:
# x += 5  es igual a escribir  x = x + 5

numero_base = float(input("Ingresa el número base: "))
valor_operacion = float(input("Ingresa el número para operar: "))

print("============================")

antes = numero_base
numero_base += valor_operacion
print(f"numero_base += {valor_operacion}    →   era {antes}, ahora es = {numero_base}")

numero_base = antes
numero_base -= valor_operacion
print(f"numero_base -= {valor_operacion}    →   era {antes}, ahora es = {numero_base}")

numero_base = antes
numero_base *= valor_operacion
print(f"numero_base *= {valor_operacion}    →   era {antes}, ahora es = {numero_base}")

numero_base = antes
numero_base **= valor_operacion
print(f"numero_base **= {valor_operacion}   →   era {antes}, ahora es = {numero_base}")

# Nota: Las siguientes operaciones de división fallarán (ZeroDivisionError) si valor_operacion es 0.0
numero_base = antes
numero_base /= valor_operacion
print(f"numero_base /= {valor_operacion}    →   era {antes}, ahora es = {numero_base}")

numero_base = antes
numero_base //= valor_operacion
print(f"numero_base //= {valor_operacion}   →   era {antes}, ahora es = {numero_base}")

numero_base = antes
numero_base %= valor_operacion
print(f"numero_base %= {valor_operacion}    →   era {antes}, ahora es = {numero_base}")

print("============================")
