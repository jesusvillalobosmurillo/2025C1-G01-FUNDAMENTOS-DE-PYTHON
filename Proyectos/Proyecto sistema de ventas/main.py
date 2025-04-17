"""
Autor: Jesus Villalobos
Fecha: 2025-04-16
Vesion: 0.1
Sistema de Gestión de Ventas que nos permita ingresar, almacenar y analizar datos de ventas.
"""
import os

from modulo import ingresar_ventas



    

def limpiar_pantalla():
    """ Limpia la pantalla en la terminal en ejecución"""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    input('\n Presione Enter para continuar...') #<-- Pausa el sistema hasta que el usuario presione Enter
    
    
# Menu principal
def menu():
    ventas = [] # Variable del sistema
    while True:
        print('\n ---- Menu Principal ----')
        print('1. Ingresar ventas de cursos UMCA')
        print('2. Guardas datos en archivo CVS')
        print ('3. Analizar ventas')
        print('4. Salir')
        opcion = input('Ingrese una opción: ')
        
        if opcion == '1':
            print('\n ----Ingresar ventas de cursos UMCA----')
            ingresar_ventas(ventas)   
            pausar()
        elif opcion == '2':
            print('\n ----Guardar datos en archivo CVS----')
            pausar()
        elif opcion == '3':
            print('\n ----Analizar ventas----')   
            pausar()   
        elif opcion == '4':
            print('\n Gracias por usar el sistema. Hasta pronto!')
            pausar()
            break #<-- Cierro el sistema deteniendo el ciclo while
        else:
            print('\n Opción no válida. Intente nuevamente una opción.')
            





        
        
#Ejecucion del sistema si solo si el archivo es el main
if __name__ == "__main__":
    print('Bienvenido al sistema de gestión de ventas')
    menu()
    