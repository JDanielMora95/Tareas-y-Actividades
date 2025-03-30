edad = int(input("Introduce tu edad: "))

if edad < 0:
    print("Edad invalida, introduce la edad correctamente")
elif edad < 13:
    print("Eres un niño")
elif edad < 18:
    print("Eres un adolecente")
elif edad >= 18 <= 30:
    print("Eres un adulto joven")
elif edad < 60:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")

# 1. ¿Qué sucedería si no incluyéramos el else?
#    R: El programa no imprimiría nada si el número es cero.
# 2. ¿Cómo cambiarías el código para incluir una categoría "adulto joven" de 18 a 29 años?
#    R: Se agrega un elif con la condición >=18 <= 30.
# 3. ¿Qué pasaría si alguien introduce una edad negativa?
#    R: Se debería manejar con otra condición para evitar errores.
