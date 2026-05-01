def mist(c,s):
    i = 0
    f = True
    p = ""
    ct = 0
    while i < len(s):
        if s[i] == "-":
            f = False
        elif f:
            p += s[i]
        if s[i] == ";":
            if p == c:
                ct += 1
            p = ""
            f = True
        i += 1
    return ct

def es_valido(sobre):
    #"AGUA-C;SOL-R;LUZ-UR;AS-C;"
    sol = mist("SOL", sobre)
    AS = mist("AS", sobre)
    #estos son los contadores de sol y as, ya que deben ser iguales para tener bien todo
    rareza = ""
    #esto es para ir guardando la rareza del sobre
    C = 0
    R = 0
    UR = 0
    #contadores de las rarezas, el sobre se determina por su rareza
    if sol == AS:
        oracion = ""
        contador = 0
        while contador < len(sobre):
            if sobre[contador] == "-":
                oracion = sobre[contador+1:]
                contador2 = 0
                while contador2 < len(oracion):
                    if oracion[contador2]== ";":
                        oracion = oracion[:contador2]
                    contador2 += 1
                if oracion == "C":
                    C += 1
                elif oracion == "R":
                    R += 1
                elif oracion == "UR":
                    UR += 1
            contador += 1
        if C > R and C > UR:
            return "C"
        elif R > C and R > UR:
            return "R"
        elif UR > C and UR > R:
            return "UR"
        #esto fué sólo filtrado para saber qué rareza es, devuelve la rareza que tenga mayor número
        if UR == R or UR == C:
            return "UR"
        if R == UR or R == C:
            return "R"
        #Y esto son los casos extras de si son iguales
        #no les tengan miedo a los if, yo lo estoy haciendo con puros if para que lo
        #entiendan mejor pero se puede optimizar (pero en un certamen no le tengan)
        #miedo a poner varias condicionales, haganlo si quieren mientras esté bueno
    else:
        return("no válido")
        #si no es válido, lo dice
    
#Pregunta 3, debe pedir sobres hasta que se ponga la palabra "salir", por ende
#como sabemos la condición, será un while. (ya que un for se utiliza cuando tenemos
#un punto de cierre)
palabra = ""
validos = 0
conteo = 0
while palabra != "salir":
    palabra = input("Ingrese sobre: ")
    if palabra.lower() != "salir":
        print(es_valido(palabra))
        #esto imprimirá la rareza en caso de que la palabra sea distinto de salir
        if es_valido(palabra) != "no válido":
            validos += 1
            conteo += 1
        else:
            conteo +=1
        #estos son validadores, basicamente saber el conteo final de validos + conteo para sacar el porcentaje

#al final, tenemos que imprimir la proporcion (porcentaje) redondeado de sobres validos respecto al total
proporcion = (validos/conteo) * 100
print("Proporción de sobres válidos ingresados:", round(proporcion), "%")
