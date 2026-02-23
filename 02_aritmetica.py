# ============================================
# OPERADORES NUMÉRICOS EN PYTHON 🧮
# ============================================

# Pedimos dos números al usuario
a = eval(input("Ingresa el primer número: "))
b = eval(input("Ingresa el segundo número: "))

# ---- OPERACIONES ----

suma        = a + b    # Suma
resta       = a - b    # Resta
multi       = a * b    # Multiplicación
potencia    = a ** b   # Potenciación (a elevado a b)
div_real    = a / b    # División real (con decimales)
div_entera  = a // b   # División entera (sin decimales)
resto       = a % b    # Resto o módulo (lo que sobra de dividir)

# ---- RESULTADOS ----

print("============================")
print("Suma:            ", suma)
print("Resta:           ", resta)
print("Multiplicación:  ", multi)
print("Potenciación:    ", potencia)
print("División real:   ", div_real)
print("División entera: ", div_entera)
print("Resto:           ", resto)
print("============================")
