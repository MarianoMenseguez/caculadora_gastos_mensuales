# gastos.py
import csv

def pedir_gastos():
    gasto_por_categoria = {
        "comida": 0.0,
        "alquiler": 0.0,
        "auto": 0.0,
        "vida cotidiana": 0.0,
        "ahorros": 0.0
    }
    
    for categoria in gasto_por_categoria:
        gasto = input(f"Ingresa el gasto {categoria}:  ")
        try:
            gasto_por_categoria[categoria] = float(gasto)
        except ValueError:
            print("Entrada inválida. Debe ser un número.")  
            gasto_por_categoria[categoria] = 0.0
    return gasto_por_categoria

def guardar_gastos_csv(gastos, nombre_archivo="registro_gastos.csv"):
    with open(nombre_archivo, "w", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Categoría", "Monto"])  # encabezado
        for categoria, monto in gastos.items():
            writer.writerow([categoria, monto])
def guardar_resumen_csv(ingreso, gastos, total, sobrante, archivo="registro_gastos.csv"):
    with open(archivo, "w", newline="") as file:
        writer = csv.writer(file)

        # Escribir ingreso
        writer.writerow(["Ingreso mensual", ingreso])

        # Línea vacía
        writer.writerow([])

        # Encabezado de gastos
        writer.writerow(["Categoría", "Monto"])

        # Escribir gastos por categoría
        for categoria, monto in gastos.items():
            writer.writerow([categoria, monto])

        # Línea vacía
        writer.writerow([])

        # Escribir total gastado y sobrante
        writer.writerow(["Total gastado", total])
        writer.writerow(["Sobrante", sobrante])