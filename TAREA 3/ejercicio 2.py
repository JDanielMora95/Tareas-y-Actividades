intentos = 0
while intentos < 3:
    usuario = input ("Usuario: ")
    password = input ("Contraseña: ")
    if usuario == "admin" and password == "secreto123":
        print ("Acceso concedido.")
        break
    elif usuario != "admin":
        print ("Usuario incorrecto.")
    else:
        print ("Contraseña incorrecta.")
    intentos += 1
else:
    print ("Acceso denegado. Demasiados intentos fallidos.")

# 1. ¿Qué operadores lógicos se usan en el código?
#    R: Se usa 'and' para validar ambas condiciones y '!=' para comparar valores.
# 2. ¿Por qué es importante validar el usuario antes que la contraseña?
#    R: Por seguridad y eficiencia, evitando intentos innecesarios.
# 3. ¿Cómo implementarías un intento fallido limitado a 3 veces?
#    R: Usando un contador y un bucle while para controlar los intentos.