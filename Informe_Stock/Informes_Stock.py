import json

def generar_informe_stock():
    with open('datos/stock.json', 'r') as file:
        data = json.load(file)
    
    print("Informe de Stock:\n")
    for categoria, productos in data.items():
        print(f"\nCategoría: {categoria}")
        for nombre, cantidad in productos.items():
            print(f"- {nombre}: {cantidad}")

