respuesta = ""
intentos = 3
while respuesta.lower() != "python" and intentos:
    respuesta = input ("¿Cuál es el mejor lenguaje de programación?: ")
    intentos += 1
if respuesta == "python":
    print ("¡Correcto!")
else:
    print ("Lo siento, has agotado tus intentos.")

# 1. ¿Qué pasaría si el usuario nunca escribe la palabra correcta?
#    R: El programa entraría en un bucle infinito.
# 2. ¿Cómo agregarías un número máximo de intentos?
#    R: Usando una variable de contador.
# 3. ¿Puedes cambiar el programa para que no importe si escriben “Python” con mayúscula?
#    R: Convirtiendo la entrada a minúsculas antes de compararla.