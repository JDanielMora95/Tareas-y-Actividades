import pandas as pd

# Crear un DataFrame 
datos = {
    "nombre": ["Juan", "Ana", "Carlos", "Laura", "Marta"],
    "edad": [25, 32, 40, 18, 29],
    "ciudad": ["CDMX", "Monterrey", "Guadalajara", "CDMX", "Puebla"]
}

df = pd.DataFrame(datos)

# Filtrar personas con edad mayor a 30 años
mayores_30 = df[df["edad"] > 30]

print("Personas mayores de 30 años:")
print(mayores_30)
