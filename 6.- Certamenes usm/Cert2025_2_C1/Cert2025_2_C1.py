def validar(pedido):
    p = 0
    for c in pedido:
        if c == "[":
            p += 1
        elif c == "]":
            p -= 1
        elif c not in "HVQTLÑCPKMZB":
            return False
        elif abs(p) > 1:
            return False
    if p == 0:
        return True
    return False

def costo_pedido(pedido):
    if not validar(pedido):
        return "Error en el pedido"
    resultado = ""
    numero_s = 0
    preciototal = 0
    corcheteabierto = False

    for c in pedido:
        if c == "[":
            corcheteabierto = True
            numero_s += 1
            preciototal = 100
        elif c == "]":
            corcheteabierto = False
            resultado += "S" + str(numero_s) + ": $" + str(preciototal) +"; "
        elif corcheteabierto:
            if c in "HVP":
                preciototal += 1000
            elif c in "QB":
                preciototal += 700
            elif c in "TLCNÑ":
                preciototal += 500
            elif c in "KMZ":
                preciototal += 300


    return resultado

sandwichestotales = -100000
nombresandwich = ""
nombreactual = ""

while nombreactual != "FIN":
    nombreactual = input("Nombre Cliente: ")
    if nombreactual != "FIN":
        pedido = input("Ingrese Pedido: ")
        detalle = costo_pedido(pedido)
        print(detalle)
        if detalle != "Error en el pedido":
            cantidad = 0
            for cor in pedido:
                if cor == "[":
                    cantidad += 1
            if cantidad > sandwichestotales:
                sandwichestotales = cantidad
                nombresandwich = nombreactual
print(nombresandwich, "pidió la mayor cantidad de hamburguesas: ", sandwichestotales)
