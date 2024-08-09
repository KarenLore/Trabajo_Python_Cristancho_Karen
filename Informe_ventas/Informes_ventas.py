import json
from datetime import datetime

def generar_informe_ventas():
    fecha_inicio = input("Ingrese la fecha de inicio del período (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin del período (YYYY-MM-DD): ")

    with open('datos/ventas.json', 'r') as file:
        data = json.load(file)
    
    ventas = data["ventas"]
    total_ingresos = 0

    print(f"\nInforme de Ventas del {fecha_inicio} al {fecha_fin}:\n")
    for venta in ventas:
        fecha_venta = datetime.strptime(venta["fecha"], "%Y-%m-%d")
        if fecha_inicio <= venta["fecha"] <= fecha_fin:
            print(f"Fecha: {venta['fecha']}")
            print(f"Cliente: {venta['cliente']['nombre']}")
            print(f"Dirección: {venta['cliente']['direccion']}")
            print(f"Empleado: {venta['empleado']['nombre']} ({venta['empleado']['cargo']})")
            print("Productos vendidos:")
            for producto in venta["productos"]:
                print(f"- {producto['nombre']} (Cantidad: {producto['cantidad']}, Precio: {producto['precio']})")
                total_ingresos += producto["cantidad"] * producto["precio"]
            print("-" * 30)

    print(f"Total Ingresos: {total_ingresos}")

