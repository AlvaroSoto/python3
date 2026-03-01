# ============================================
# FUNCIONES INTEGRADAS DE PYTHON
# ============================================

separador = "=" * 44

# ============================================
# 1. int()  ->  convierte un valor a entero
# ============================================
# int(x)        convierte x a entero (trunca, no redondea)
# int(texto)    convierte texto numérico a entero
# int(x, base)  convierte texto en la base indicada a entero

print(separador)
print("int()")
print(separador)

print(int(9.99))          # 9   <- trunca, NO redondea
print(int(-3.7))          # -3
print(int("42"))          # 42  <- texto a número
print(int("1010", 2))     # 10  <- binario "1010" a decimal
print(int("FF",  16))     # 255 <- hexadecimal a decimal


# ============================================
# 2. eval()  ->  evalúa una expresión en texto
# ============================================
# eval(expresion)   ejecuta la expresion como si fuera código Python
# Útil para calcular fórmulas almacenadas como texto.
#
# ⚠️  ADVERTENCIA: nunca uses eval() con datos del usuario,
#     ya que ejecutaría código arbitrario en tu máquina.

print(separador)
print("eval()  - ejemplo de álgebra: f(x) = 4x² + 32")
print(separador)

x = 3
resultado = eval("4 * x**2 + 32")   # usa la variable x del contexto
# Paso a paso:  4 * 3² + 32  =  4 * 9 + 32  =  36 + 32  =  68
print(f"x = {x}")
print(f"eval('4 * x**2 + 32') = {resultado}")   # 68


# ============================================
# 3. round()  ->  redondea un número
# ============================================
# round(numero)          redondea al entero más cercano
# round(numero, n)       redondea a n decimales

print(separador)
print("round(numero, decimales)")
print(separador)

print(round(3.14159))        # 3
print(round(3.14159, 2))     # 3.14
print(round(3.14159, 4))     # 3.1416
print(round(2.5))            # 2  <- Python usa "redondeo bancario" (al par más cercano)
print(round(3.5))            # 4
print(round(-2.675, 2))      # -2.67  <- cuidado con la precisión del float


# ============================================
# 4. abs()  ->  valor absoluto (siempre positivo)
# ============================================
# abs(x)   devuelve el valor absoluto de x

print(separador)
print("abs(x)  - valor absoluto")
print(separador)

print(abs(-15))      # 15
print(abs(7))        # 7
print(abs(-3.75))    # 3.75


# ============================================
# 5. max()  ->  valor mayor de una secuencia
# ============================================
# max(iterable)         mayor elemento de la lista/tupla/cadena
# max(a, b, c, ...)     mayor entre varios valores separados por comas

print(separador)
print("max()  - valor mayor")
print(separador)

numeros = [4, 7, 1, 9, 3]
print(max(numeros))          # 9  <- mayor en la lista
print(max(5, 12, 3, 8))      # 12 <- mayor entre argumentos
print(max("python"))         # y  <- mayor carácter según su código ASCII


# ============================================
# 6. min()  ->  valor menor de una secuencia
# ============================================
# min(iterable)         menor elemento de la lista/tupla/cadena
# min(a, b, c, ...)     menor entre varios valores separados por comas

print(separador)
print("min()  - valor menor")
print(separador)

print(min(numeros))          # 1  <- menor en la lista
print(min(5, 12, 3, 8))      # 3  <- menor entre argumentos
print(min("python"))         # h  <- menor carácter según su código ASCII


# ============================================
# 7. pow()  ->  potencia
# ============================================
# pow(base, exp)         base elevado a exp  (igual que base ** exp)
# pow(base, exp, mod)    (base ** exp) % mod  (útil en criptografía)

print(separador)
print("pow(base, exp)  /  pow(base, exp, mod)")
print(separador)

print(pow(2, 10))          # 1024  <- 2^10
print(pow(3, 3))           # 27    <- 3^3
print(pow(2, 10, 100))     # 24    <- 1024 % 100


# ============================================
# 8. format()  ->  da formato a números y texto
# ============================================
# format(valor, especificador)
#
# Especificadores comunes:
#   'd'      entero decimal
#   'b'      binario
#   'o'      octal
#   'x'      hexadecimal (minúsculas)
#   'X'      hexadecimal (mayúsculas)
#   'f'      float con decimales fijos
#   '.nf'    float con n decimales
#   ',f'     float con separador de miles
#   'e'      notación científica
#   '<n'     alineado a la izquierda en n caracteres
#   '>n'     alineado a la derecha  en n caracteres
#   '^n'     centrado en n caracteres

print(separador)
print("format(valor, especificador)")
print(separador)

# --- Enteros ---
print(format(255, 'd'))     # 255    <- decimal (por defecto)
print(format(255, 'b'))     # 11111111  <- binario
print(format(255, 'o'))     # 377    <- octal
print(format(255, 'x'))     # ff     <- hexadecimal minúsculas
print(format(255, 'X'))     # FF     <- hexadecimal mayúsculas
print(format(42,  '08b'))   # 00101010  <- binario relleno con ceros a 8 dígitos

# --- Floats ---
print(format(3.14159, '.2f'))      # 3.14
print(format(3.14159, '.4f'))      # 3.1416
print(format(1234567.89, ',.2f'))  # 1,234,567.89  <- separador de miles
print(format(0.000123, 'e'))       # 1.230000e-04  <- notación científica
print(format(0.000123, '.2e'))     # 1.23e-04

# --- Texto (alineación) ---
print(format("Python", '<12'))     # 'Python      '  <- izquierda
print(format("Python", '>12'))     # '      Python'  <- derecha
print(format("Python", '^12'))     # '   Python   '  <- centro
print(format("Python", '*^12'))    # '***Python***'  <- centro con relleno *


# ============================================
# 9. print()  ->  imprime en pantalla
# ============================================
# print(*objetos, sep=' ', end='\n', flush=False)
#
#   *objetos   uno o más valores a imprimir, separados por comas
#   sep        texto entre cada valor (por defecto: espacio ' ')
#   end        texto al final (por defecto: salto de línea '\n')
#   flush      True fuerza la escritura inmediata en el buffer

print(separador)
print("print()  - parametros sep y end")
print(separador)

# sep: cambia el separador entre valores
print("Lunes", "Martes", "Miércoles")                  # sep=" " por defecto
print("Lunes", "Martes", "Miércoles", sep=", ")        # Lunes, Martes, Miércoles
print("Lunes", "Martes", "Miércoles", sep=" | ")       # Lunes | Martes | Miércoles
print(1, 2, 3, sep="-")                                # 1-2-3

# end: cambia lo que se imprime al final de la línea
print("Primera línea", end=" ")   # no hace salto, sigue en la misma línea
print("Segunda línea")            # Primera línea Segunda línea

print("Cargando", end="")
print("...")                       # Cargando...

# Varios valores y tipos a la vez (print los convierte a str automáticamente)
edad = 25
print("Tengo", edad, "años y mido", 1.75, "metros")


# ============================================
# 10. str()  ->  convierte un valor a cadena de texto
# ============================================
# str(x)   convierte x a su representación en texto

print(separador)
print("str(x)  - conversión a cadena")
print(separador)

print(str(42))           # '42'
print(str(3.14))         # '3.14'
print(str(True))         # 'True'
print(str(None))         # 'None'

# Útil para concatenar texto con números
puntaje = 150
mensaje = "Tu puntaje es: " + str(puntaje)
print(mensaje)           # Tu puntaje es: 150


# ============================================
# 11. chr()  ->  carácter desde su código ASCII
# ============================================
# chr(codigo)  devuelve el carácter Unicode correspondiente al código
# ord(caracter) hace lo inverso: devuelve el código de un carácter

print(separador)
print("chr(codigo)  y  ord(caracter)")
print(separador)

print(chr(65))    # A
print(chr(97))    # a
print(chr(48))    # 0  <- dígito cero
print(chr(9829))  # corazón (♥)

# ord() hace lo inverso
print(ord('A'))   # 65
print(ord('a'))   # 97
print(ord('0'))   # 48

# Recorrer el abecedario usando chr() y range()
abecedario = ""
for codigo in range(65, 91):      # 65=A  hasta 90=Z
    abecedario += chr(codigo)
print(abecedario)                 # ABCDEFGHIJKLMNOPQRSTUVWXYZ


# ============================================
# 12. OPERADORES CON CADENAS
# ============================================

print(separador)
print("Operadores con cadenas")
print(separador)

a = "Hola"
b = " Mundo"

# +  concatenación: une dos cadenas
print(a + b)              # Hola Mundo

# *  repetición: repite la cadena n veces
print("Ha" + "r" * 6)    # Harrrrrrr
print("-" * 20)           # --------------------

# len()  longitud: cantidad de caracteres
print(len("Python"))      # 6
print(len(""))            # 0

# in / not in  pertenencia
print("Hola" in "Hola Mundo")       # True
print("hola" in "Hola Mundo")       # False <- sensible a mayúsculas
print("Java" not in "Hola Mundo")   # True

# []  indexación: accede a un carácter por su posición (empieza en 0)
texto = "Python"
print(texto[0])    # P  <- primer carácter
print(texto[-1])   # n  <- último carácter
print(texto[-2])   # o  <- penúltimo carácter

# [inicio:fin]  slicing: extrae una porción de la cadena
#   inicio  posición donde comienza (incluida)
#   fin     posición donde termina  (NO incluida)
#   paso    de cuánto en cuánto avanza
print(texto[0:3])     # Pyt  <- posiciones 0, 1, 2
print(texto[2:])      # thon <- desde posición 2 hasta el final
print(texto[:4])      # Pyth <- desde el inicio hasta posición 3
print(texto[::2])     # Pto  <- de 2 en 2
print(texto[::-1])    # nohtyP <- invertida

print(separador)
