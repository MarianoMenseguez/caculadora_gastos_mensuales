# Función para mostrar total gastado y sobrante
from gastos import pedir_gastos
from ingreso import pedir_ingreso

def calcular_total(gasto_por_categoria):
    total=sum(gasto_por_categoria.values())
    return total

def calcular_sobrante(ingreso_mensual,total):
    sobrante = ingreso_mensual - total
    return sobrante 
    