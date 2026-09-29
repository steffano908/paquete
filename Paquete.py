cajas = []


def precioPorKilo(caja):
    return caja["precio"] / caja["peso"]


def ordenarPorRatio(lista):
    n = len(lista)
    posActual = 0
    while posActual < n:
        mayor = posActual
        posVista = posActual
        while posVista < n:
            if precioPorKilo(lista[posVista]) > precioPorKilo(lista[mayor]):
                mayor = posVista
            paso = 1
            posVista = posVista + paso
        aux = lista[posActual]
        lista[posActual] = lista[mayor]
        lista[mayor] = aux
        paso = 1
        posActual = posActual + paso
    return lista


def llenarMochila(lista, capacidad):
    ordenarPorRatio(lista)
    pesoLlevado = 0
    ganancia = 0
    print('----- CAJAS SELECCIONADAS -----')
    for caja in lista:
        if pesoLlevado < capacidad:
            disponible = capacidad - pesoLlevado
            if caja["peso"] <= disponible:
                pesoParcial = caja["peso"]
                solesParcial = caja["precio"]
                porcentaje = 100
            else:
                porcentaje = (disponible / caja["peso"]) * 100
                pesoParcial = disponible
                solesParcial = caja["precio"] * (porcentaje / 100)
            pesoLlevado = pesoLlevado + pesoParcial
            ganancia = ganancia + solesParcial
            print(f'{caja["nombre"]}: {porcentaje:.1f}% - {pesoParcial:.2f} kg - S/ {solesParcial:.2f}')
            if pesoLlevado == capacidad:
                break
    print('-------------------------------')
    print(f'Peso total: {pesoLlevado:.2f} kg')
    print(f'Ganancia total: S/ {ganancia:.2f}')


cajas.append({"nombre": "A", "peso": 10, "precio": 4})
cajas.append({"nombre": "B", "peso": 4, "precio": 3})
cajas.append({"nombre": "C", "peso": 7, "precio": 3})
cajas.append({"nombre": "D", "peso": 5, "precio": 2})
cajas.append({"nombre": "E", "peso": 3, "precio": 1})
cajas.append({"nombre": "F", "peso": 3, "precio": 2})
cajas.append({"nombre": "G", "peso": 2, "precio": 1.8})
cajas.append({"nombre": "H", "peso": 3, "precio": 3})

capacidad = float(input('Ingrese peso maximo de la mochila: '))

llenarMochila(cajas, capacidad)