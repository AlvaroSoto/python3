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

# 5. CONVERSIÓN DE DATOS (int/float)
#    Para operar matemáticamente, convertimos el texto a número de forma segura.
edad = int(input("¿Cuántos años tienes? "))
print(f"En 10 años tendrás {edad + 10} años")

# ⚠️ NOTA SOBRE EVAL():
# Se puede usar eval() para calcular expresiones en texto, por ejemplo:
resultado_eval = eval("10 + 10") 
# Pero es MUY RIESGOSO usarlo directamente con input() porque un usuario 
# podría escribir código malicioso que eval() ejecutaría en tu computadora.
