import pandas as pd

# Cargar el archivo CSV (reemplaza 'data.csv' con tu archivo real)
df = pd.read_csv("pruebas.csv", encoding = "latin1")
'''print(type(df))
# Mostrar las primeras filas del dataset
print("Primeras 5 filas del dataset:")
print(df.head())'''

'''# Mostrar tipos de datos de cada columna
print("\nTipos de datos:")'''
print(df.dtypes)

'''# Mostrar estadísticas básicas
print("\nEstadísticas descriptivas:")
print(df.describe())'''
