# main.py

from pyfiglet import Figlet
import random
import sqlite3
import requests

def bienvenido_titulo():
    figlet = Figlet()
    fuentes_disponibles = figlet.getFonts()
    fuente_seleccionada = random.choice(fuentes_disponibles)
    figlet.setFont(font=fuente_seleccionada)
    titulo = "Bienvenido"
    print(figlet.renderText(titulo))

def contar_palabra_la(texto):
    return texto.lower().count("la")

def configurar_aplicacion():
    # Conectar a la base de datos y crear tablas
    conexion = sqlite3.connect('base_de_datos.db')
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tipo_cambio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            moneda TEXT,
            cambio REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            direccion TEXT
        )
    ''')

    conexion.commit()
    conexion.close()

def actualizar_tipo_cambio():
    # Obtener datos de la API de tipo de cambio
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    respuesta = requests.get(url)
    datos_tipo_cambio = respuesta.json()

    # Conectar a la base de datos y actualizar la tabla tipo_cambio
    conexion = sqlite3.connect('base_de_datos.db')
    cursor = conexion.cursor()

    for moneda, cambio in datos_tipo_cambio.items():
        cursor.execute('INSERT INTO tipo_cambio (moneda, cambio) VALUES (?, ?)', (moneda, cambio))

    conexion.commit()
    conexion.close()

def editar_precio():
    # Lógica para editar el precio
    print("Editando precio...")

def editar_stock():
    # Lógica para editar el stock
    print("Editando stock...")

def buscar_producto_por_nombre():
    nombre_producto = input("Ingrese el nombre del producto a buscar: ")
    # Lógica para buscar el producto por nombre en la base de datos
    print(f"Buscando producto por nombre: {nombre_producto}...")

def agregar_cliente():
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    direccion_cliente = input("Ingrese la dirección del cliente: ")
    # Lógica para agregar el cliente a la base de datos
    print(f"Agregando cliente: {nombre_cliente}, Dirección: {direccion_cliente}...")

def listar_clientes():
    # Lógica para listar los clientes en la base de datos
    print("Listando clientes...")

if __name__ == "__main__":
    configurar_aplicacion()
    
    bienvenido_titulo()
    while True:
        print("1. Hacer algo")
        print("2. Editar título")
        print("3. Actualizar tipo de cambio desde API")
        print("4. Editar precio")
        print("5. Editar stock")
        print("6. Buscar producto por nombre")
        print("7. Agregar cliente")
        print("8. Listar clientes")
        print("9. Salir")
        
        seleccion = input("Seleccione una opción: ")
        if seleccion == "1":
            # Lógica para la Opción 1
            print("Haciendo algo...")
        elif seleccion == "2":
            bienvenido_titulo()
        elif seleccion == "3":
            actualizar_tipo_cambio()
            print("Tipo de cambio actualizado.")
        elif seleccion == "4":
            editar_precio()
        elif seleccion == "5":
            editar_stock()
        elif seleccion == "6":
            buscar_producto_por_nombre()
        elif seleccion == "7":
            agregar_cliente()
        elif seleccion == "8":
            listar_clientes()
        elif seleccion == "9":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")