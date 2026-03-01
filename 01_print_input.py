# ============================================
# MI PRIMER PROGRAMA EN PYTHON 🐍
# ============================================

# 1. IMPRIMIR EN PANTALLA
print("¡Hola Mundo!")

# 2. UNA VARIABLE (guarda un dato)
nombre = "Ana"
print("La variable nombre vale:", nombre)  # "Ana"

# 3. INPUT (pedirle algo al usuario, reemplaza el valor anterior)
nombre = input("¿Cómo te llamas? ")

# 4. F-STRING (forma moderna de incluir variables dentro de un texto)
print(f"¡Hola, {nombre}!")

# 5. EVAL (convierte texto a número para operar, igual que int/float pero más flexible)
#    eval("42")    → 42   (entero)
#    eval("3.14")  → 3.14 (decimal)
#    eval("2 + 2") → 4    (¡incluso evalúa expresiones matemáticas en el texto!)
# 
# ⚠️ IMPORTANTE: Aunque eval() es útil para aprender o probar, es MUY RIESGOSO usarlo con 
#    lo que ingresa el usuario (input). Si el usuario escribe código malicioso, eval() lo ejecutará.
#    En la vida real, para números siempre es preferible usar int() para enteros o float() para decimales.
edad = eval(input("¿Cuántos años tienes? (puedes escribir 20 o 10+10) "))
print(f"En 10 años tendrás {edad + 10} años")
