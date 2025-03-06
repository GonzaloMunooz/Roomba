import concurrent.futures

# Función para calcular el área de una zona
def calcular_area(largo, ancho):
    return largo * ancho

# Función de interpolación lineal
def lerp(a, b, t):
    return a + (b - a) * t

def calcular_areas(zonas):
    areas = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_zona = {
            executor.submit(calcular_area, largo, ancho): zona
            for zona, (largo, ancho) in zonas.items()
        }
        for future in concurrent.futures.as_completed(future_to_zona):
            zona = future_to_zona[future]
            try:
                area = future.result()
            except Exception as exc:
                print(f"{zona} generó una excepción: {exc}")
            else:
                areas[zona] = area
                print(f"{zona}: {area} cm²")
    return areas

def main():
    zonas = {
        'Zona 1': (500, 150),
        'Zona 2': (480, 101),
        'Zona 3': (309, 480),
        'Zona 4': (90, 220)
    }
    
    tasa_limpeza = 1000
    
    areas = calcular_areas(zonas)
    
    superficie_total = sum(areas.values())
    tiempo_limpeza = superficie_total / tasa_limpeza
    
    print(f"\nSuperficie total a limpiar: {superficie_total} cm²")
    print(f"Tiempo estimado de limpieza: {tiempo_limpeza:.2f} segundos")
    
    juego = Juego()
    juego.run()

if __name__ == '__main__':
    main()
