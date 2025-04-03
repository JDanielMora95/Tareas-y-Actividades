import numpy as np

# Crear dos matrices 3x3 con valores aleatorios del 1 al 10
A = np.random.randint(1, 11, (3, 3))
B = np.random.randint(1, 11, (3, 3))

# Operaciones básicas
suma = A + B
resta = A - B
multiplicacion = A * B  # Elemento a elemento

print("Matriz A:")
print(A)

print("\nMatriz B:")
print(B)

print("\nSuma de matrices:")
print(suma)

print("\nResta de matrices:")
print(resta)

print("\nMultiplicación elemento a elemento:")
print(multiplicacion)
