codigo_secreto = {
        3: "5 + 4 - 6",
        7: "3 * 3 - 2",
        2: "10 // 5",
        9: "8 + 1",
        4: "16 // 4"
    }
    
    print("¡Bienvenido al juego del código secreto!")
    respuestas_correctas = 0
    for clave, expresion in codigo_secreto.items():
        respuesta = int(input(f"Resuelve: {expresion} = "))
        if respuesta == clave:
            respuestas_correctas += 1
        else:
            print("Respuesta incorrecta. Acceso denegado.")
            return
    
    if respuestas_correctas == len(codigo_secreto):
        print("¡Código Descifrado! Has ganado.")
