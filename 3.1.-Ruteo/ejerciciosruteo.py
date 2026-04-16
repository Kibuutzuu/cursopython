total = 0
limite = 4

for i in range(1, limite):
    if i % 2 == 0:
        total = total + (i * 2)
    else:
        total = total + i

print(f"Resultado final: {total}")


def calcular(n):
    res = 0
    while n > 0:
        if n % 2 == 0:
            res = res + n
        else:
            res = res + 1
        n = n - 1
    return res

valor = 4
final = calcular(valor)
print(final)


def proceso(limite):
    x = 0
    puntos = 0
    while x < limite:
        if x == 2:
            puntos += 10
            x += 3
        else:
            puntos += 2
            x += 1
    return puntos

resultado = proceso(6)
print(resultado)


def formatear_palabra(texto):
    resultado = ""
    indice = 0
    largo = len(texto)
    
    while indice < largo:
        letra = texto[indice]
        if indice == largo - 1:
            resultado = resultado + letra + ";"
        else:
            resultado = resultado + letra + "-"
        indice = indice + 1
        
    return resultado

palabra = "char"
print(formatear_palabra(palabra))