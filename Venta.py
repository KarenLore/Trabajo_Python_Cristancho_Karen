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
            producto = input("Nombre del producto: ").strip()

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

                agregar_otro = input("¿Deseas agregar otro producto? (s/n): ").strip().lower()
                if agregar_otro != 's':
                    break
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
        "Pan de Bono": 700,
        "Pan de Queso": 800,
        "Pan Cascarita": 500,
        "Pan de Yuca": 800,
        "Calentano": 700,
        "Rollito de Sal": 900,
        "Pan Integral": 700,
        "Pan relleno de Arequipe": 1150,
        "Pan con Salchicha": 1300,
        "Pan recubierto de Chocolate": 1200
    },
    "Pasteleria": {
        "Pastel de Vainilla": 5000,
        "Pastel de Chocolate": 5500,
        "Pastel de bodas": 10000,
        "Glaseado de Vainilla": 3000,
        "Glaseado de Chocolate": 3500,
        "Pastel de Arequipe": 5700,
        "Pastel de Oreo": 7000,
        "Postre de Limón": 4300,
        "Postre de Vainilla": 4000,
        "Postre de Tres Leches": 4500
    },
    "Bebidas": {
        "Coca-Cola": 3000,
        "Pepsi": 2900,
        "Red-Bull": 4000,
        "Gatorade": 3700,
        "Budweiser": 3200,
        "Hit": 2500,
        "Pony-Malta": 2300,
        "Sprite": 3200,
        "Monster": 3000,
        "Tropicana": 2400,
        "-Promociones-": "Algunas promociones de la sección de Bebidas",
        "1 Pan con Salchicha y 1 Pony Malta": 3000,
        "1 Postre de Oreo y 1 Budweiser": 9000
    },
    "Apartado de promociones": {
        "6 Panes Integrales": 4000,
        "5 Panes recubiertos de Chocolate": 5500,
        "3 Pasteles de Vainilla": 13000,
        "4 Postres de Oreo": 25000,
        "1 Pan con Salchicha y 1 Pony Malta": 3000,
        "1 Postre de Oreo y 1 Budweiser": 9000
    }
}

# Ejecución del registro de venta
if __name__ == "__main__":
    registrar_venta()
