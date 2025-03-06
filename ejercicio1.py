import concurrent.futures
import pygame
import random


def calcular_area(largo, ancho):
    """Calcula el área de una zona multiplicando largo por ancho."""
    return largo * ancho

def lerp(a, b, t):
    """Interpolación lineal entre a y b."""
    return a + (b - a) * t

class Acro:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.color = (0, 255, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

    def is_touched(self, roomba_x, roomba_y, roomba_size):
        return (self.x - roomba_x)**2 + (self.y - roomba_y)**2 < (self.size + roomba_size)**2

def main():
    # Definición de las zonas con sus dimensiones (largo, ancho)
    zonas = {
        'Zona 1': (500, 150),
        'Zona 2': (480, 101),
        'Zona 3': (309, 480),
        'Zona 4': (90, 220)
    }
    
    # Tasa de limpieza (por ejemplo, 1000 cm²/segundo)
    tasa_limpeza = 1000  # cm²/s
    
    # Diccionario para almacenar el área calculada de cada zona
    areas = {}
    
    # Uso de ThreadPoolExecutor para ejecutar los cálculos de forma concurrente
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Asignamos cada cálculo a un hilo
        future_to_zona = {
            executor.submit(calcular_area, largo, ancho): zona
            for zona, (largo, ancho) in zonas.items()
        }
        
        # Recogemos los resultados a medida que se van completando
        for future in concurrent.futures.as_completed(future_to_zona):
            zona = future_to_zona[future]
            try:
                area = future.result()
            except Exception as exc:
                print(f"{zona} generó una excepción: {exc}")
            else:
                areas[zona] = area
                print(f"{zona}: {area} cm²")
                
    # Calcular la superficie total sumando las áreas parciales
    superficie_total = sum(areas.values())
    # Calcular el tiempo de limpieza
    tiempo_limpeza = superficie_total / tasa_limpeza
    
    print(f"\nSuperficie total a limpiar: {superficie_total} cm²")
    print(f"Tiempo estimado de limpieza: {tiempo_limpeza:.2f} segundos")
    
    # Inicialización de Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Roomba en movimiento")
    
    # Colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    
    # Posición inicial de la Roomba
    x, y = 400, 300
    roomba_size = 20
    
    # Posición objetivo inicial (misma que la posición inicial)
    target_x, target_y = x, y
    
    # Crear una lista de ácaros

    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Actualizar la posición objetivo al hacer clic en la pantalla
                target_x, target_y = event.pos
        
        # Mover la Roomba suavemente hacia la nueva posición objetivo
        x = lerp(x, target_x, 0.1)
        y = lerp(y, target_y, 0.1)
        
        # Dibujar la pantalla
        screen.fill(WHITE)
        
        # Dibujar la Roomba
        pygame.draw.circle(screen, RED, (int(x), int(y)), roomba_size)
        
        # Dibujar y verificar colisiones con los ácaros
        for acaro in acaros[:]:
            if acaro.is_touched(x, y, roomba_size):
                acaros.remove(acaro)
            else:
                acaro.draw(screen)
        
        pygame.display.flip()
        
        clock.tick(30)
    
    pygame.quit()

def spawnzombies():

    def spawnmultiplezombies():
         numero_aleatorio = random.randint(1, 10)
         for i in range(1,numero_aleatorio):
            
  

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Asignamos cada cálculo a un hilo
        future_to_zombis = {
            executor.submit(calcular_area, largo, ancho): zona
            for zona, (largo, ancho) in zonas.items()
        }
        
        # Recogemos los resultados a medida que se van completando
        for future in concurrent.futures.as_completed(future_to_zona):
            zona = future_to_zona[future]
            try:
                area = future.result()
            except Exception as exc:
                print(f"{zona} generó una excepción: {exc}")
            else:
                areas[zona] = area
                print(f"{zona}: {area} cm²")
   
    
if __name__ == '__main__':
    main()
