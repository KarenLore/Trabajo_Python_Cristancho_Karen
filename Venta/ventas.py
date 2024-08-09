import json
from datetime import datetime

def registrar_venta():
    venta = {
        "fecha": input("Ingrese la fecha de la venta (YYYY-MM-DD): "),
        "cliente": {
            "nombre": input("Ingrese el nombre del cliente: "),
            "direccion": input("Ingrese la dirección del cliente: ")
        },
        "empleado": {
            "nombre": input("Ingrese el nombre del empleado: "),
            "cargo": input("Ingrese el cargo del empleado: ")
        },
        "productos": []
    }

    while True:
        producto = {
            "nombre": input("Ingrese el nombre del producto: "),
            "cantidad": int(input("Ingrese la cantidad: ")),
            "precio": float(input("Ingrese el precio: "))
        }
        venta["productos"].append(producto)
        
        continuar = input("¿Desea agregar otro producto? (s/n): ")
        if continuar.lower() != "s":
            break
    
    with open('datos/ventas.json', 'r') as file:
        data = json.load(file)
    
    data["ventas"].append(venta)
    
    with open('datos/ventas.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("Venta registrada con éxito.")
