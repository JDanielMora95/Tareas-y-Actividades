'''numero = int(input("Introduce un numero: "))
for i in range(10, 0, -1):
    print(f"{numero} x {i} = {numero * i}")'''

#
for numero in range(1,11):
    print(f"Tabla del {numero}:")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")
    print()

# 1. ¿Qué hace range(1, 11) exactamente?
#    R: Genera números del 1 al 10.
# 2. ¿Cómo podrías modificar el código para imprimir la tabla al revés?
  #    R: Usando range(10, 0, -1).
# 3. ¿Cómo harías que imprima todas las tablas del 1 al 10?
#    R: Usando un bucle anidado para recorrer los números del 1 al 10.