# editor
import pygame
import sys

class pixel:
  def __init__(self,x:int,y:int,z:int):
    self.x = x
    self.y = y
    self.z = z 

# --- Настройки ---
height = int(input("height (1-8?): "))
GRID_SIZE = 50           # Сетка 50 на 50
CELL_SIZE = 15           # Размер одной клетки в пикселях
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
pixels = []
# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)

# Инициализация
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Pixel Map Editor 50x50")

# Создаем пустую карту (двумерный массив 50x50)
# 0 - пусто, 1 - закрашено
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

clock = pygame.time.Clock()

def draw_grid():
  screen.fill(WHITE)
  
  # Рисуем закрашенные клетки
  for y in range(GRID_SIZE):
    for x in range(GRID_SIZE):
      if grid[y][x] == 1:
        pygame.draw.rect(screen, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

  # Рисуем сетку (линии)
  for i in range(GRID_SIZE + 1):
    # Вертикальные линии
    pygame.draw.line(screen, GRAY, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE))
    # Горизонтальные линии
    pygame.draw.line(screen, GRAY, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE))
    
  pygame.display.flip()

# Главный цикл программы
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
        
    # Отслеживаем клик мыши
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1: # Левая кнопка мыши
        mouse_x, mouse_y = event.pos
        
        # Переводим пиксели экрана в координаты сетки
        grid_x = (mouse_x // CELL_SIZE)
        grid_y = (mouse_y // CELL_SIZE)
        
        # Проверяем, что кликнули внутри сетки
        if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
          # Если клетка пустая - закрашиваем, если закрашена - очищаем
          if grid[grid_y][grid_x] == 0:
            grid[grid_y][grid_x] = 1
          else:
            grid[grid_y][grid_x] = 0
              
          # Выводим координаты в консоль
          for y in range(height):
            pixels += [pixel(grid_x - GRID_SIZE//2, y, grid_y - GRID_SIZE//2)]

  draw_grid()
  clock.tick(60) # 60 кадров в секунду

pygame.quit()