"""
Gestor de gastos personales en consola, hecho en Python.

Proyecto académico de Ingeniería en Informática (Duoc UC).
Permite registrar gastos con descripción, monto y categoría desde un
menú interactivo, y ver resúmenes con totales, promedio y gasto mayor.

Autor: Diego Valenzuela
"""


def pedir_monto():
    """Pide un monto válido (número mayor que cero)."""
    while True:
        try:
            monto = int(input("Monto ($): "))
            if monto <= 0:
                print("  -> El monto debe ser mayor que cero.")
                continue
            return monto
        except ValueError:
            print("  -> Entrada inválida. Escribe solo números, sin puntos ni comas.")


def agregar_gasto(gastos):
    descripcion = input("Descripción del gasto: ").strip()
    if not descripcion:
        print("  -> La descripción no puede estar vacía.")
        return
    monto = pedir_monto()
    categoria = input("Categoría (ej: comida, transporte, útiles): ").strip()
    if not categoria:
        categoria = "otros"

    gastos.append({
        "descripcion": descripcion,
        "monto": monto,
        "categoria": categoria.lower(),
    })
    print(f"  -> Gasto registrado: {descripcion} - ${monto:,} ({categoria})")


def listar_gastos(gastos):
    if not gastos:
        print("  -> Todavía no hay gastos registrados.")
        return
    print("\n--- Tus gastos ---")
    for i, gasto in enumerate(gastos, start=1):
        print(f"{i}. {gasto['descripcion']} - ${gasto['monto']:,} [{gasto['categoria']}]")


def mostrar_resumen(gastos):
    if not gastos:
        print("  -> Todavía no hay gastos registrados.")
        return

    total = sum(g["monto"] for g in gastos)
    promedio = total / len(gastos)
    mayor = max(gastos, key=lambda g: g["monto"])

    # Total agrupado por categoría
    por_categoria = {}
    for g in gastos:
        por_categoria[g["categoria"]] = por_categoria.get(g["categoria"], 0) + g["monto"]

    print("\n--- Resumen ---")
    print(f"Cantidad de gastos: {len(gastos)}")
    print(f"Total gastado:      ${total:,}")
    print(f"Promedio por gasto: ${promedio:,.0f}")
    print(f"Gasto mayor:        {mayor['descripcion']} - ${mayor['monto']:,}")
    print("\nTotal por categoría:")
    for categoria, monto in sorted(por_categoria.items(), key=lambda x: -x[1]):
        print(f"  - {categoria}: ${monto:,}")


def mostrar_menu():
    print("\n======= GESTOR DE GASTOS =======")
    print("1. Agregar gasto")
    print("2. Ver mis gastos")
    print("3. Ver resumen")
    print("0. Salir")
    print("================================")


def main():
    gastos = []

    print("Bienvenido a tu gestor de gastos en Python")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "0":
            print("¡Hasta luego!")
            break
        elif opcion == "1":
            agregar_gasto(gastos)
        elif opcion == "2":
            listar_gastos(gastos)
        elif opcion == "3":
            mostrar_resumen(gastos)
        else:
            print("  -> Opción no válida. Elige un número del menú.")


if __name__ == "__main__":
    main()