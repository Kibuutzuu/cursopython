def misterio(s):
    i = 2
    m = int(s[0])
    while i<len(s):
        if int(s[i]) > m:
            m = int(s[i])
        i += 2
    return m


def filas_secas(invernadero, umbral):
    contadorinicio = 0
    contadorfin = 0
    contadorzonas = 0
    fila = ""
    o = 0
    while o < len(invernadero):
        if invernadero[o] == "|":
            fila = invernadero[contadorinicio:contadorfin]
            num = misterio(fila)
            if num < umbral:
                contadorzonas += 1
            contadorinicio = contadorfin + 1
        elif o == len(invernadero) -1:
            fila = invernadero[contadorinicio:contadorfin+1]
            num = misterio(fila)
            if num < umbral:
                contadorzonas += 1
            contadorinicio = contadorfin + 1
        contadorfin += 1
        o+= 1

    return contadorzonas


umbral = int(input("Ingrese valor umbral: "))
secas = 1
minimo = 10000000000000
maximo = 0
consideracion = 0
while secas != 0:
    pregunta = input("Ingrese estado de un invernadero:")
    secas = filas_secas(pregunta, umbral)
    print("Secas: ", secas)
    if secas!=0:
        promedio = 0
        contador = 0
        for i in pregunta:
            if i in "123456789":
                promedio += int(i)
                contador += 1
        promedio = round(promedio/contador)
        consideracion += 1
        print("Humerdad promedio:", promedio)
        if promedio < minimo:
            minimo = promedio
        elif promedio > maximo:
            maximo = promedio
    else:
        print("El invernadero no tiene secciones secas")
print("Invernaderos considerados:", consideracion)
print("Humedad promedio maxima:", maximo)
print("Humedad promedio minima:", minimo)
