from ast import main
from PRUEBAFINALPYTHON.validaciones import agregar_arreglo, agregar_arreglo, validar_codigo, validar_color, validar_color, validar_nombre, validar_nombre, validar_precio, validar_tamano, validar_tarjeta, validar_temporada, validar_tipo, validar_unidades
import validaciones
arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno']
}
bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6]
}
while True:
    opcion = validaciones.leer_opcion()
    if opcion == 1:
        tipo = input("Ingrese tipo de arreglo: ")
        validaciones.unidades_tipo(tipo, arreglos, bodega)
    elif opcion == 2:
        while True:
            try:
                precio_min = int(input("Ingrese precio mínimo: "))
                precio_max = int(input("Ingrese precio máximo: "))
                if precio_min >= 0 and precio_max >= 0 and precio_min <= precio_max:
                    break
                print("Debe ingresar un rango válido.")
            except ValueError:
                print("Debe ingresar valores enteros")
        validaciones.busqueda_precio(precio_min, precio_max, arreglos, bodega)
    elif opcion == 3:
        while True:
            codigo = input("Ingrese código: ")
            while True:
                try:
                    nuevo_precio = int(input("Nuevo precio: "))
                    if nuevo_precio > 0:
                        break
                    print("Debe ingresar un precio mayor que cero.")
                except ValueError:
                    print("Debe ingresar un número entero.")
            if validaciones.actualizar_precioalizar_precio(codigo, nuevo_precio, bodega):
                print("Precio actualizado")
            else:
                print("El código no existe")
            respuesta = input("¿Desea actualizar otro precio (s/n)? ").lower()
            if respuesta == "n":
                break
            elif opcion == 4:
                codigo = input("Código: ").upper()
                nombre = input("Nombre: ")
                tipo = input("Tipo: ")
                color = input("Color principal: ")
                tamano = input("Tamaño (S/M/L): ").upper()
                tarjeta = input("¿Incluye tarjeta? (s/n): ").lower()
                temporada = input("Temporada: ")
        try:
            precio = int(input("Precio: "))
            unidades = int(input("Unidades: "))
        except ValueError:
            print("Precio y unidades deben ser números enteros.")
            continue
        if not validar_codigo(codigo):
            print("Código inválido.")
            continue
        if validaciones.buscar_codigo(codigo, bodega):
            print("El código ya existe")
            continue
        if not validar_nombre(nombre):
            print("Nombre inválido.")
            continue
        if not validar_tipo(tipo):
            print("Tipo inválido.")
            continue
        if not validar_color(color):
            print("Color inválido.")
            continue
        if not validar_tamano(tamano):
            print("Tamaño inválido.")
            continue
        if not validar_tarjeta(tarjeta):
            print("Debe ingresar s o n.")
            continue
        if not validar_temporada(temporada):
            print("Temporada inválida.")
            continue
        if not validar_precio(precio):
            print("Precio inválido.")
            continue
        if not validar_unidades(unidades):
            print("Cantidad de unidades inválida.")
            continue
        incluye_tarjeta = tarjeta == "s"
        if agregar_arreglo(
                codigo,
                nombre,
                tipo,
                color,
                tamano,
                incluye_tarjeta,
                temporada,
                precio,
                unidades,
                arreglos,
                bodega):
            print("Arreglo agregado")
        else:
            print("El código ya existe")
    elif opcion == 5:
        codigo = input("Ingrese código del arreglo: ")
        if validaciones.eliminar_arreglo(codigo, arreglos, bodega):
            print("Arreglo eliminado")
        else:
            print("El código no existe")
    elif opcion == 6:
        print("Programa finalizado.")
        break
if __name__=="__main__":
    main()