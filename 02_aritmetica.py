# ============================================
# OPERADORES NUMÉRICOS EN PYTHON 🧮
# ============================================

# Pedimos dos números al usuario (float acepta enteros y decimales)
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

# ---- OPERACIONES ----

suma        = a + b    # Suma
resta       = a - b    # Resta
multi       = a * b    # Multiplicación
potencia    = a ** b   # Potenciación (a elevado a b)
div_real    = a / b    # División real (con decimales)
div_entera  = a // b   # División entera (sin decimales)
resto       = a % b    # Resto o módulo (lo que sobra de dividir)

# ---- RESULTADOS (se muestra la operación completa para mayor claridad) ----

print("============================")
print(f"Suma:            {a} + {b} = {suma}")
print(f"Resta:           {a} - {b} = {resta}")
print(f"Multiplicación:  {a} * {b} = {multi}")
print(f"Potenciación:    {a} ** {b} = {potencia}")
print(f"División real:   {a} / {b} = {div_real}")
print(f"División entera: {a} // {b} = {div_entera}")
print(f"Resto:           {a} % {b} = {resto}")
print("============================")
