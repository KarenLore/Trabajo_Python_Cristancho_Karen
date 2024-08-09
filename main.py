from Venta import registrar_venta
from Compra import registrar_compra
from Informes import generar_informe_ventas, generar_informe_stock

def main():
    while True:
        "#############BIENVENIDOS###############"
        print("\nMenú Principal PanCamp")
        print("1. Registrar Venta")
        print("2. Registrar Compra")
        print("3. Generar Informe de Ventas")
        print("4. Generar Informe de Stock")
        print("5. Cerrar Sesión")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_venta()
        elif opcion == '2':
            registrar_compra()
        elif opcion == '3':
            generar_informe_ventas()
        elif opcion == '4':
            generar_informe_stock()
        elif opcion == '5':
            print("Hasta luego!!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

