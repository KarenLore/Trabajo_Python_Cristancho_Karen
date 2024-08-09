import json
from datetime import datetime

def registrar_venta():
    venta = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cliente": {
            "nombre": input("Nombre del cliente: "),
            "direccion": input("Dirección del cliente: ")
        },
        "empleado": {
            "nombre": input("Nombre del empleado: "),
            "cargo": input("Cargo del empleado: ")
        },
        "productos": []
    }

    print("Seleccione una categoría:")
    print("1. Panaderia")
    print("2. Pasteleria")
    print("3. Bebidas")
    print("4. Apartado de promociones")

    categoria = input("Seleccione una opción: ")

    categorias = {
        '1': "Panaderia",
        '2': "Pasteleria",
        '3': "Bebidas",
        '4': "Apartado de promociones"
    }

    if categoria in categorias:
        categoria_seleccionada = categorias[categoria]
        print(f"\nCategoría seleccionada: {categoria_seleccionada}")

        while True:
            producto = input("Nombre del producto (o 'no' para terminar): ")
            if producto.lower() == 'no':
                break

            if producto in productos[categoria_seleccionada]:
                precio = productos[categoria_seleccionada][producto]

                print(f"Precio de {producto}: {precio}")

                while True:
                    cantidad_input = input(f"Cantidad de {producto}: ")
                    if cantidad_input.isdigit():
                        cantidad = int(cantidad_input)
                        break
                    else:
                        print("Por favor, ingrese un número válido para la cantidad.")
                
                venta["productos"].append({
                    "nombre": producto,
                    "cantidad": cantidad,
                    "precio": precio
                })
            else:
                print("El producto ingresado no existe en la categoría seleccionada.")

        with open('ventas.json', 'a') as file:
            json.dump(venta, file, indent=4)
            file.write("\n")

        print("Venta registrada exitosamente.")
    else:
        print("Categoría no válida.")

# Estructura actualizada de precios y categorías
productos = {
    "Panaderia": {
        "Pan de Bono": 70,
        "Pan de Queso": 80,
        "Pan Cascarita": 50,
        "Pan de Yuca": 80,
        "Calentano": 70,
        "Rollito de Sal": 90,
        "Pan Integral": 70,
        "Pan relleno de Arequipe": 115,
        "Pan con Salchicha": 130,
        "Pan recubierto de Chocolate": 120
    },
    "Pasteleria": {
        "Pastel de Vainilla": 500,
        "Pastel de Chocolate": 550,
        "Pastel de bodas": 100,
        "Glaseado de Vainilla": 300,
        "Glaseado de Chocolate": 350,
        "Pastel de Arequipe": 570,
        "Pastel de Oreo": 700,
        "Postre de Limón": 430,
        "Postre de Vainilla": 400,
        "Postre de Tres Leches": 450
    },
    "Bebidas": {
        "Coca-Cola": 300,
        "Pepsi": 290,
        "Red-Bull": 400,
        "Gatorade": 370,
        "Budweiser": 320,
        "Hit": 250,
        "Pony-Malta": 230,
        "Sprite": 320,
        "Monster": 300,
        "Tropicana": 240,
        "-Promociones-": "Algunas promociones de la sección de Bebidas",
        "1 Pan con Salchicha y 1 Pony Malta": 300,
        "1 Postre de Oreo y 1 Budweiser": 900
    },
    "Apartado de promociones": {
        "6 Panes Integrales": 400,
        "5 Panes recubiertos de Chocolate": 550,
        "3 Pasteles de Vainilla": 1300,
        "4 Postres de Oreo": 2500,
        "1 Pan con Salchicha y 1 Pony Malta": 300,
        "1 Postre de Oreo y 1 Budweiser": 900
    }
}