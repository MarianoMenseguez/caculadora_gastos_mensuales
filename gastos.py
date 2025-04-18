# Funciones para ingresar y manejar gastos

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
            gasto_por_categoria[categoria]=float(gasto)
        except ValueError:
            print("Entrada inválida. Debe ser un número.")  
            gasto_por_categoria[categoria]=0.0
    return gasto_por_categoria             