import os 
from getpass import getpass
from tabulate import tabulate
from conexion import *
import usuario
import contrasena

conexion = conectar()
crear_tablas(conexion)

def inicio():
    os.system('cls')
    comprobar = usuario.comprobar_usuario()
    if len(comprobar) == 0:
        print('Bienvenido, registre su informacion')
        nombre = input('Ingrese su nombre: ')
        apellido = input('Ingrese su apellido: ')
        contrasena_maestra = getpass('Ingrese su contraseña maestra: ')
        respuesta = usuario.registrar(nombre, apellido, contrasena_maestra)
        if respuesta == 'Registro correcto':
            print(f'Bienvenido {nombre}')
            menu()
        else:
            print(respuesta)
    else:
        contrasena_maestra = getpass('Ingrese su contraseña maestra: ')
        respuesta = usuario.comprobar_contrasena(1, contrasena_maestra)
        if len(respuesta) == 0:
            print('Contraseña incorrecta')
        else:
            print('Bienvenido')
            menu()
def menu():
    while True:
        print('Seleccione una de las siguientes opciones: ')
        print('\t1- Añadir contraseña')
        print('\t2- Ver todas las contraseñas')
        print('\t3- Visualizar una contraseña')
        print('\t4- Modificar una contraseña')
        print('\t5- Eliminar una contraseña')
        print('\t6- Salir')
        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            print('Añadiendo contraseña...')
            nueva_contrasena()
        elif opcion == '2':
            print('Visualizando contraseñas...')
            mostrar_contrasenas()
        elif opcion == '3':
            print('Visualizando contraseña...')
            buscar_contrasena()
        elif opcion == '4':
            print('Modificando contraseña...')
            modificar_contrasena()
        elif opcion == '5':
            print('Eliminando contraseña...')
            eliminar_contrasena()
        elif opcion == '6':
            print('Saliendo...')
            break
        else:
            print('No ingreso una opcion valida')

def nueva_contrasena():
    nombre = input('Ingrese el nombre: ')
    url = input('Ingrese el url: ')
    nombre_usuario = input('Ingrese el nombre_usuario: ')
    contraseña = input('Ingrese la contrasena: ')
    descripcion = input('Ingrese la descripcion: ')
    respuesta = contrasena.registrar(nombre, url, nombre_usuario, contraseña, descripcion)
    print(respuesta)

def mostrar_contrasenas():
    datos = contrasena.mostrar()
    nuevos_datos = []
    headers = ['ID', 'NOMBRE', 'URL', 'USUARIO', 'CONTRASEÑA', 'DESCRIPCION']
    for dato in datos:
        convertido = list(dato)
        convertido[4] = '*******'
        nuevos_datos.append(convertido)

    tabla = tabulate(nuevos_datos, headers, tablefmt='fancy_grid')
    print('\t\t\t\tTodas las contraseñas')
    print(tabla)

def buscar_contrasena():
    contasena_maestra = getpass('Ingrese su contraseña maestra: ')
    respuesta = usuario.comprobar_contrasena(1, contasena_maestra)
    if len(respuesta) == 0:
        print('Contraseña incorrecta')
    else:
        id = input('Ingrese el id de la contraseña a buscar: ')
        datos = contrasena.buscar(id)
        headers = ['ID', 'NOMBRE', 'URL', 'USUARIO', 'CONTRASEÑA', 'DESCRIPCION']
        tabla = tabulate(datos, headers, tablefmt='fancy_grid')
        print('\t\t\t\tTodas las contraseñas')
        print(tabla)

def modificar_contrasena():
    contasena_maestra = getpass('Ingrese su contraseña maestra: ')
    respuesta = usuario.comprobar_contrasena(1, contasena_maestra)
    if len(respuesta) == 0:
        print('Contraseña incorrecta')
    else:
        id = input('Ingrese el id de la contraseña a modificar: ')
        nombre = input('Ingrese el nombre de la contraseña a modificar: ')
        url = input('Ingrese el url de la contraseña a modificar: ')
        nombre_usuario = input('Ingrese el nombre_usuario de la contraseña a modificar: ')
        contraseña = input('Ingrese el contrasena de la contraseña a modificar: ')
        descripcion = input('Ingrese el descripcion de la contraseña a modificar: ')
        respuesta = contrasena.modificar(id, nombre, url, nombre_usuario, contraseña, descripcion)
        print(respuesta)

def eliminar_contrasena():
    contasena_maestra = getpass('Ingrese su contraseña maestra: ')
    respuesta = usuario.comprobar_contrasena(1, contasena_maestra)
    if len(respuesta) == 0:
        print('Contraseña incorrecta')
    else:
        id = input('Ingrese el id de la contraseña a eliminar: ')
        respuesta = contrasena.eliminar(id)
        print(respuesta)

inicio()