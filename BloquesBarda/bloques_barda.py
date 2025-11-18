from math import ceil

def costo_barda(largo_muro, alto_muro):
    alto_bloque = 0.20
    largo_bloque = 0.40
    precio_bloque = 19.80
    desperdicio = 0.05

    area_muro = largo_muro * alto_muro
    area_bloque = alto_bloque * largo_bloque

    bloques = area_muro / area_bloque
    bloques *= (1 + desperdicio)
    bloques = ceil(bloques)

    costo_total = bloques * precio_bloque

    return bloques, costo_total


def main():
    print("=== Calculadora de bloques para barda ===")

    try:
        largo = float(input("Introduce el largo del muro (m): "))
        alto = float(input("Introduce la altura del muro (m): "))

        bloques, costo = costo_barda(largo, alto)

        print("\n--- RESULTADOS ---")
        print(f"Bloques necesarios: {bloques}")
        print(f"Costo total: ${costo:.2f} MXN")

    except ValueError:
        print("ERROR: Debes ingresar valores numéricos válidos.")

if __name__ == "__main__":
    main()