stock_entradas = [150, 180]
entradas_vendidas = [0, 0]

compradores = []

def mostrar_menu():
    print("TOTEM AUTOATENCIÓN CAFECONLECHE")
    print("1.- Comprar entrada a Cats.")
    print("2.- Cambio de función.")
    print("3.- Mostrar stock_entradas de funciones.")
    print("4.- Salir.")

def mostrar_stock_entradas():
    print("-- stock_entradas de Funciones --")
    print(f"Función 1 (Viernes) : Disponibles {stock_entradas[0]}, Vendidas {entradas_vendidas[0]}")
    print(f"Función 2 (Sábado) : Disponibles {stock_entradas[1]}, Vendidas {entradas_vendidas[1]}")

def comprar_entrada():
    print("-- Comprar entrada a Cats --")
    nombre = input("Nombre del comprador: ").strip()

    print(f"Seleccione función:")
    print(f"1. Cats Día Viernes ({stock_entradas[0]} entradas)")
    print(f"2. Cats Día Sábado ({stock_entradas[1]} entradas)")

    try:
        funcion = int(input("Función (1 ó 2): "))
        if funcion not in [1, 2]:
            raise ValueError
    except ValueError:
        print("Error: opción de función inválida.")
        return

    entradas = funcion - 1
    if stock_entradas[entradas] > 0:
        compradores.append([nombre, funcion])
        stock_entradas[entradas] -= 1
        entradas_vendidas[entradas] += 1
        print(f"Entrada registrada en función {funcion}! stock_entradas restantes:")
        mostrar_stock_entradas()
    else:
        print("No hay entradas disponibles para esta función. :(")

def cambiar_funcion():
    print("-- Cambio de función --")
    nombre = input("Nombre del comprador: ").strip()

    for comprador in compradores:
        if comprador[0].lower() == nombre.lower():
            funcion_actual = comprador[1]
            funcion_nueva = 2 if funcion_actual == 1 else 1
            respuesta = input(f"Cambiar de función {funcion_actual} a {funcion_nueva}? (S/N): ").strip().lower()

            if respuesta != 's':
                print("Cambio cancelado.")
                return

            nueva_entradas = funcion_nueva - 1
            actual_entradas = funcion_actual - 1

            if stock_entradas[nueva_entradas] > 0:
                stock_entradas[actual_entradas] += 1
                entradas_vendidas[actual_entradas] -= 1

                stock_entradas[nueva_entradas] -= 1
                entradas_vendidas[nueva_entradas] += 1

                comprador[1] = funcion_nueva
                print(f"Cambio exitoso. Ahora está en función {funcion_nueva}.")
            else:
                print("No hay stock_entradas disponible para la nueva función.")
            return

        print("Error: comprador no encontrado.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            comprar_entrada()
        elif opcion == "2":
            cambiar_funcion()
        elif opcion == "3":
            mostrar_stock_entradas()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!")

if __name__ == "__main__":
    main()
