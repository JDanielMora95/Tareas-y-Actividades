'''palabra = input ("Escribe una frase: ")
contador = 0
for letra in palabra:
    if letra.isalpha (): # Solo cuenta letras
        contador += 1
print ("Numero de letras:",contador)'''

#

'''palabra = input ("Escribe una frase: ")
contador = 0
vocales = "aeiouAEIOU"
for letra in palabra:
    if letra in vocales:
        contador += 1
print ("Numero de vocales:",contador)'''

#

palabra = input ("Escribe una frase: ")
contador = 0
for letra in palabra:
    contador += 1
print ("Numero de caracteres:",contador)

# 1. ¿Qué otros caracteres podrías querer ignorar además de espacios?
#    R: Signos de puntuación, números, tabulaciones y saltos de línea.
# 2. ¿Cómo podrías contar solo vocales?
#    R: Filtrando solo caracteres en "aeiouAEIOU".
# 3. ¿Qué pasa si no usas if?
#    R: Se contarían todos los caracteres sin distinción.
