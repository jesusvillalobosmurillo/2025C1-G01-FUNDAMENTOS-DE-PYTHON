import csv, os, pandas as pd

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
            
            
            
def guardar_ventas(ventas):
    if not ventas:
        print('No hay ventas que guardar en el CSV')
    else:
        if os.path.exists('ventas.csv'):
            #Append
            with open('ventas.csv','a',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['curso','cantidad','precio','fecha','cliente'])
                guardar.writerows(ventas)           
        else: # Si no existe el archivo, lo crea y guarda los datos
            with open('ventas.csv','w',newline='',encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo,fieldnames=['curso','cantidad','precio','fecha','cliente'])
                guardar.writeheader()
                guardar.writerows(ventas)
            print ('Datos guardados exitosamente')
            
        # Limpia las ventas en memoria y muestra lo guardado exitoso
        ventas = [] 
        print ('Datos Guardados exitosamente')

        
def analisis_ventas():
    df = pd.read_csv('ventas.csv')
    print ('\n ------------------ Resumen de Ventas ------------------')
    
    df ['subtotal'] = df['cantidad'] * df['precio']
    total_ingresos = df['subtotal'].sum()
    
    print(f'Total de ventas: {total_ingresos:,.2f}')
    
    #curso mas vendido
    curso_top = df.groupby('curso')['cantidad'].sum().idxmax()
    print(f'Curso más vendido: ', curso_top)
    
    # cliente mas frecuente
    cliente_top = df.groupby('cliente')['cantidad'].sum().idxmax()
    print(f'Cliente más frecuente: ', cliente_top)
    
    # Total por fechas
    fechas_top = df.groupby('fecha')['subtotal'].sum().sort_values(ascending=False)
    print(f'Fecha con mayor venta: ', fechas_top)