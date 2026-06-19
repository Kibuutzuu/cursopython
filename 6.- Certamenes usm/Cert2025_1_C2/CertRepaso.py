def mas_ocupados(nombre_archivo, fecha1, fecha2):
    archivo = open(nombre_archivo)
    d = {}
    consulta = False
    for i in archivo:
        if consulta:
            idpaciente, fecha, hora, especialista, especialidad, tipo = i.strip().split(
                ";"
            )
            if fecha1 <= fecha <= fecha2:
                if especialista not in d:
                    d[especialista] = 0
                d[especialista] += 1
        else:
            consulta = True
    archivo.close()
    lista = []
    for i in d:
        lista.append([d[i], i])
    lista.sort()
    lista.reverse()
    for i in range(len(lista)):
        lista[i] = lista[i][1]
    return lista[:3]


def agenda_por_tipo(nombre_archivo, tipo_consulta):
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    filtrada = 0
    total = 0
    considerar = False
    d = {}
    for linea in archivo:
        if considerar:
            idpaciente, fecha, hora, especialista, especialidad, tipo = (
                linea.strip().split(";")
            )
            total += 1
            if tipo == tipo_consulta:
                filtrada += 1
                if especialidad not in d:
                    d[especialidad] = []
                d[especialidad].append([fecha, hora, especialista, tipo])
        else:
            considerar = True
    archivo.close()

    for especialidad_iterable in d:
        d[especialidad_iterable].sort()
        archivo = open("{}_{}.txt".format(tipo_consulta, especialidad_iterable), "w")
        archivo.write(
            "Citas de {} en formato {} \n".format(especialidad_iterable, tipo_consulta)
        )
        for fecha, hora, especialista, tipo in d[especialidad_iterable]:
            archivo.write("{} {}: {}. \n".format(fecha, hora, especialista))
        archivo.close()
    porcentaje = round(100 * filtrada / total, 2)
    return "{} representa el {}% de todas las citas".format(tipo_consulta, porcentaje)


print("Pregunta 1")
print(mas_ocupados("citas.csv", "2025/06/26", "2025/06/30"))
print("\n\nPregunta2")
print(agenda_por_tipo("citas.csv", "Telemedicina"))
