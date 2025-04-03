import numpy as np

# Paso 1: Crear un array aleatorio de 10 números entre 1 y 100
array = np.random.randint(1, 101, size=10)
print("Array original:", array)

# Paso 2: Calcular estadísticas
media = np.mean(array)
maximo = np.max(array)
minimo = np.min(array)
desviacion = np.std(array)

print(f"Media: {media}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Desviación estándar: {desviacion}")

# Paso 3: Multiplicar todos los elementos por 2
array_doble = array * 2
print("Array multiplicado por 2:", array_doble)
