def leer_opcion():
    while True:
        try:
            print("""
========== MENÚ PRINCIPAL ==========
1. Unidades por tipo de arreglo
2. Búsqueda de arreglos por rango de precio
3. Actualizar precio de arreglo
4. Agregar arreglo
5. Eliminar arreglo
6. Salir
=====================================
""")
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")
def validar_codigo(codigo):
    if codigo.strip() == "":
        return False
    return True
def validar_nombre(nombre):
    if nombre.strip() == "":
        return False
    return True
def validar_tipo(tipo):
    if tipo.strip() == "":
        return False
    return True
def validar_color(color):
    if color.strip() == "":
        return False
    return True
def validar_tamano(tamano):
    tamano = tamano.upper()
    if tamano in ("S", "M", "L"):
        return True
    return False
def validar_tarjeta(tarjeta):
    tarjeta = tarjeta.lower()
    if tarjeta == "s":
        return True
    if tarjeta == "n":
        return True
    return False
def validar_temporada(temporada):
    if temporada.strip() == "":
        return False
    return True
def validar_precio(precio):
    if precio > 0:
        return True
    return False
def validar_unidades(unidades):
    if unidades >= 0:
        return True
    return False
def buscar_codigo(codigo, bodega):
    codigo = codigo.upper()
    for cod in bodega.keys():
        if cod.upper() == codigo:
            return True
    return False
def unidades_tipo(tipo, arreglos, bodega):
    total = 0
    tipo = tipo.lower()
    for codigo in arreglos:
        if arreglos[codigo][1].lower() == tipo:
            total += bodega[codigo][1]
    print(f"Total de unidades: {total}")
def busqueda_precio(p_min, p_max, arreglos, bodega):
    lista = []
    for codigo in bodega:
        precio = bodega[codigo][0]
        unidades = bodega[codigo][1]
        if precio >= p_min and precio <= p_max and unidades > 0:
            nombre = arreglos[codigo][0]
            lista.append(f"{nombre}--{codigo}")
    if len(lista) == 0:
        print("No hay arreglos en ese rango de precios.")
    else:
        lista.sort()
        print("\nArreglos encontrados:\n")
        for arreglo in lista:
            print(arreglo)
def actualizar_precio(codigo, nuevo_precio, bodega):
    codigo = codigo.upper()
    if buscar_codigo(codigo, bodega):
        for cod in bodega:
            if cod.upper() == codigo:
                bodega[cod][0] = nuevo_precio
                return True
    return False
def agregar_arreglo(codigo,
                    nombre,
                    tipo,
                    color_principal,
                    tamano,
                    incluye_tarjeta,
                    temporada,
                    precio,
                    unidades,
                    arreglos,
                    bodega):
    codigo = codigo.upper()
    if buscar_codigo(codigo, bodega):
        return False
    arreglos[codigo] = [
        nombre,
        tipo,
        color_principal,
        tamano.upper(),
        incluye_tarjeta,
        temporada
    ]
    bodega[codigo] = [
        precio,
        unidades
    ]
    return True
def eliminar_arreglo(codigo, arreglos, bodega):
    codigo = codigo.upper()
    if buscar_codigo(codigo, bodega):

        for cod in list(arreglos.keys()):

            if cod.upper() == codigo:

                del arreglos[cod]
                del bodega[cod]

                return True
    return False