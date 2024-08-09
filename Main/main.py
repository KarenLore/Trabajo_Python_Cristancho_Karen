import sys
import os

# Añadir el directorio raíz al PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Venta.ventas import registrar_venta
from Compra.compras import registrar_compra
from Informe_ventas.Informes_ventas import generar_informe_ventas
from Informe_Stock.Informes_Stock import generar_informe_stock

def menu():
    while True:
        print("1. Registrar Venta")
        print("2. Registrar Compra")
        print("3. Generar Informe de Ventas")
        print("4. Generar Informe de Stock")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            registrar_compra()
        elif opcion == "3":
            generar_informe_ventas()
        elif opcion == "4":
            generar_informe_stock()
        elif opcion == "5":
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
