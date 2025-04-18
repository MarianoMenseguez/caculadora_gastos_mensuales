# Punto de entrada del programa
from ingreso import pedir_ingreso
from gastos import pedir_gastos
from calcular_total import calcular_total, calcular_sobrante

def main():
    ingreso= pedir_ingreso()
    gasto=pedir_gastos()
    
    total = calcular_total(gasto)
    sobrante=calcular_sobrante(ingreso, total)
    
    
    print("\n📊 RESUMEN DE GASTOS")
    print("----------------------")
    print(f"Ingreso mensual: ${ingreso}")
    print(f"Gasto total:     ${total}")
    print(f"Dinero restante: ${sobrante}")
    
if __name__ == "__main__":
    main()    