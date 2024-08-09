import csv
from datetime import datetime

ventas = [
    {"fecha": "2024-08-01", "producto": "Pan", "cantidad": 10, "precio": 20},
]

stock = [
    {"producto": "Pan", "cantidad": 50},
]

def generar_informe_ventas():
    """Genera un informe de ventas y lo guarda en un archivo CSV."""
    fecha = datetime.now().strftime("%Y-%m-%d")
    archivo = f"informe_ventas_{fecha}.csv"
    
    with open(archivo, 'w', newline='') as csvfile:
        fieldnames = ["fecha", "producto", "cantidad", "precio"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for venta in ventas:
            writer.writerow(venta)
    
    print(f"Informe de ventas generado: {archivo}")

def generar_informe_stock():
    """Genera un informe de stock y lo guarda en un archivo CSV."""
    fecha = datetime.now().strftime("%Y-%m-%d")
    archivo = f"informe_stock_{fecha}.csv"
    
    with open(archivo, 'w', newline='') as csvfile:
        fieldnames = ["producto", "cantidad"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for item in stock:
            writer.writerow(item)
    
    print(f"Informe de stock generado: {archivo}")

import csv
from datetime import datetime

stock = [
    {"producto": "Pan", "cantidad": 20},
    {"producto": "Pan de Bono", "cantidad": 30},
    {"producto": "Pan de Queso", "cantidad": 15},
    {"producto": "Pan Cascarita", "cantidad": 45},
    {"producto": "Pan de Yuca", "cantidad": 60},
    {"producto": "Calentano", "cantidad": 35},
    {"producto": "Rollito de Sal", "cantidad": 25},
    {"producto": "Pan Integral", "cantidad": 70},
    {"producto": "Pan relleno de Arequipe", "cantidad": 75},
    {"producto": "Pan con Salchicha", "cantidad": 35},
    {"producto": "Pan recubierto de Chocolate", "cantidad": 20},
    {"producto": "Pastel de Vainilla", "cantidad": 30},
    {"producto": "Pastel de Chocolate", "cantidad": 40},
    {"producto": "Pastel de bodas", "cantidad": 15},
    {"producto": "Glaseado de Vainilla", "cantidad": 28},
    {"producto": "Glaseado de Chocolate", "cantidad": 20},
    {"producto": "Pastel de Arequipe", "cantidad": 40},
    {"producto": "Pastel de Oreo", "cantidad": 44},
    {"producto": "Postre de Limón", "cantidad": 65},
    {"producto": "Postre de Vainilla", "cantidad": 18},
    {"producto": "Postre de Tres Leches", "cantidad": 26},
    {"producto": "Coca-Cola", "cantidad": 45},
    {"producto": "Pepsi", "cantidad": 60},
    {"producto": "Red-Bull", "cantidad": 54},
    {"producto": "Gatorade", "cantidad": 35},
    {"producto": "Budweiser", "cantidad": 50},
    {"producto": "Hit", "cantidad": 30},
    {"producto": "Pony-Malta", "cantidad": 15},
    {"producto": "Sprite", "cantidad": 25},
    {"producto": "Monster", "cantidad": 36},
    {"producto": "Tropicana", "cantidad": 20},
    {"producto": "Panes Integrales", "cantidad": 40},
    {"producto": "Panes recubiertos de Chocolate", "cantidad": 45},
    {"producto": "Pasteles de Vainilla", "cantidad": 50},
    {"producto": "Postres de Oreo", "cantidad": 20},
    {"producto": "Pan con Salchicha y 1 Pony Malta", "cantidad": 26},
    {"producto": "Postre de Oreo y 1 Budweiser", "cantidad": 35},

]

def generar_informe_stock():
    """Genera un informe de stock y lo guarda en un archivo CSV."""
    fecha = datetime.now().strftime("%Y-%m-%d")
    archivo = f"informe_stock_{fecha}.csv"
    
    with open(archivo, 'w', newline='') as csvfile:
        fieldnames = ["producto", "cantidad"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for item in stock:
            writer.writerow(item)
    
    print(f"Informe de stock generado: {archivo}")

if __name__ == "__main__":
    generar_informe_stock()
