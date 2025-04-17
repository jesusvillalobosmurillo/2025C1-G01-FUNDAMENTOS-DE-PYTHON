def ingresar_ventas(lista_ventas):
    while True:
        try:    
            curso = input('Ingrese el nombre del curso: ').upper()
            cantidad = int(input('Ingrese la cantidad de cursos vendidos: '))
            fecha = input('Ingrese la fecha de la venta (AAA-MM-DD): ')
            precio = float(input('Ingrese el precio del curso: '))
            cliente = input('Ingrese el nombre del cliente: ').upper()
        except ValueError:
            print('Entrada no valida. Por favor, intente nuevamente.')
            continue
        
        venta = {
            'curso': curso,
            'cantidad': cantidad,
            'fecha': fecha,
            'precio': precio,
            'cliente': cliente
        }
        lista_ventas.append(venta)
        
        continuar = input('¿Desea ingresar otra venta? (s/n): ')
        if continuar == 's':
            print('\n ----Ingresar otra venta----')
        elif continuar == 'n':
            break
        else:
            print('\n Opción no válida')