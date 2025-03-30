op = input("Elige una operacion (+, -, *, /): ")
a = int(input("Primer numero: "))
b = int(input("Segundo numero: "))

match op:
    case "+":
        print("resultado:", a + b)
    case "-":
        print("resultado:", a - b)
    case "*":
        print("resultado:", a * b)
    case "/":
        print("resultado:", a / b if b != 0 else " no se puede dividir entre cero")
    case "/":
        if b == 0:
            raise ValueError("No se puede dividir entre cero")
        print("resultado:", a / b)
    case _:
        print("operacion no valida.")

# 1. ¿Qué ventaja tiene match sobre if en este caso?
#     R: Permite una sintaxis más clara y legible.
# 2. ¿Qué pasa si el usuario pone otro símbolo?
#     R: Si el usuario ingresa un símbolo o un valor que no es uno de los esperados ("+", "-", "*", "/"), el programa imprimirá "operación no valida."
# 3. ¿Qué deberías validar antes de dividir?
#     R: Que el divisor no sea cero