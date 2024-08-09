import json

def registrar_compra():
    compra = {
        "fecha": input("Ingrese la fecha de la compra (YYYY-MM-DD): "),
        "proveedor": {
            "nombre": input("Ingrese el nombre del proveedor: "),
            "contacto": input("Ingrese el contacto del proveedor: ")
        },
        "productos": []
    }

    while True:
        producto = {
            "nombre": input("Ingrese el nombre del producto: "),
            "cantidad": int(input("Ingrese la cantidad: ")),
            "precio_compra": float(input("Ingrese el precio de compra: "))
        }
        compra["productos"].append(producto)
        
        continuar = input("¿Desea agregar otro producto? (s/n): ")
        if continuar.lower() != "s":
            break
    
    with open('datos/compras.json', 'r') as file:
        data = json.load(file)
    
    data["compras"].append(compra)
    
    with open('datos/compras.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("Compra registrada con éxito.")
