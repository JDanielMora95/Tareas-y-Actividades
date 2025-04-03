import pandas as pd

# Paso 1: Crear un DataFrame con datos de estudiantes
data = {
    "Nombre": ["Ana", "Juan", "Luis", "María", "Pedro"],
    "Edad": [22, 21, 23, 22, 20],
    "Calificación": [85, 90, 78, 88, 74]
}

df = pd.DataFrame(data)
print("DataFrame original:\n", df)

# Paso 2: Agregar un nuevo estudiante
nuevo_estudiante = pd.DataFrame({"Nombre": ["Carlos"], "Edad": [24], "Calificación": [92]})
df = pd.concat([df, nuevo_estudiante], ignore_index=True)
print("\nDataFrame con nuevo estudiante:\n", df)

# Paso 3: Filtrar estudiantes con calificación mayor a 80
filtro = df[df["Calificación"] > 80]
print("\nEstudiantes con calificación mayor a 80:\n", filtro)

# Paso 4: Calcular la media de las calificaciones
media_calificaciones = df["Calificación"].mean()
print("\nMedia de calificaciones:", media_calificaciones)
