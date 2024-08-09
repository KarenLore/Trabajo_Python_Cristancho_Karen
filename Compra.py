import json
from datetime import datetime

def obtener_datos_proveedor():
    nombre = input("Nombre del proveedor: ")
    contacto = input("Contacto del proveedor: ")
    return {"nombre": nombre, "contacto": contacto}

def obtener_datos_producto():
    productos = []
    while True:
        producto = input("Nombre del producto comprado: ").strip()
        try:
            cantidad = int(input(f"Cantidad de {producto}: "))
            precio_compra = int(input(f"Precio de compra de {producto}: "))
        except ValueError:
            print("Por favor, ingrese un valor válido para la cantidad y el precio.")
            continue
        
        productos.append({
            "nombre": producto,
            "cantidad": cantidad,
            "precio_compra": precio_compra
        })

        agregar_otro = input("¿Deseas agregar otro producto? (s/n): ").strip().lower()
        if agregar_otro != 's':
            break

    return productos

def registrar_compra():
    compra = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "proveedor": obtener_datos_proveedor(),
        "productos": obtener_datos_producto()
    }
    
    with open('compras.json', 'a') as file:
        json.dump(compra, file, indent=4)
        file.write("\n")
    
    print("Compra registrada exitosamente.")

# Ejecución del registro de compra
if __name__ == "__main__":
    registrar_compra()
