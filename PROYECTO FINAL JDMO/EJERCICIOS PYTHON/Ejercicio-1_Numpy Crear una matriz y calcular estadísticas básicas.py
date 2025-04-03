import numpy as np

# Crear una matriz 3x3 con números aleatorios del 1 al 100
matriz = np.random.randint(1, 101, (3, 3))

# Calcular estadísticas
media = np.mean(matriz)
mediana = np.median(matriz)
desviacion = np.std(matriz)

print("Matriz generada:")
print(matriz)

print(f"\nMedia: {media}")
print(f"Mediana: {mediana}")
print(f"Desviación estándar: {desviacion}")
print(f"suma de media y desviacion estandar es: {media + desviacion}")
 