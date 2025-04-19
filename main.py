# main.py
from ingreso import pedir_ingreso
from gastos import pedir_gastos, guardar_resumen_csv 
from calcular_total import calcular_total, calcular_sobrante

def main():
    ingreso = pedir_ingreso()
    gastos = pedir_gastos()
    total = calcular_total(gastos)
    sobrante = calcular_sobrante(ingreso, total)

    print(f"\nTotal gastado: ${total}")
    print(f"Sobrante: ${sobrante}")

    guardar_resumen_csv(ingreso, gastos, total, sobrante)

if __name__ == "__main__":
    main()
