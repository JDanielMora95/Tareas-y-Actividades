import random

# Crear una matriz de números aleatorios (10x10)
filas, columnas = 10, 10
matriz = [[random.randint(1, 100) for _ in range(columnas)] for _ in range(filas)]

# Convertir la matriz en una lista plana
valores = [num for fila in matriz for num in fila]

# Calcular la media
suma_total = sum(valores)
cantidad_elementos = len(valores)
media = suma_total / cantidad_elementos

# Calcular la mediana
valores_ordenados = sorted(valores)
n = cantidad_elementos
if n % 2 == 1:
    mediana = valores_ordenados[n // 2]
else:
    mediana = (valores_ordenados[n // 2 - 1] + valores_ordenados[n // 2]) / 2

# Calcular la desviación estándar
varianza = sum((x - media) ** 2 for x in valores) / cantidad_elementos
desviacion_estandar = varianza ** 0.5

# Mostrar la matriz
print("Matriz de números aleatorios:")
for fila in matriz:
    print(fila)

# Mostrar estadísticas
print("\nEstadísticas básicas:")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desviación Estándar: {desviacion_estandar:.2f}")
