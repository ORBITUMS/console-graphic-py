import time
import sys
# start = time.perf_counter()
from pynput import keyboard
from pynput.keyboard import Key, KeyCode

pressed = set() # какие клавиши сейчас зажаты
events  = [] # одноразовые события, накопленные с прошлого кадра

class pixel:
  def __init__(self,x:int,y:int,z:int):
    self.x = x
    self.y = y
    self.z = z 
    # self.distance = 0
  
  def __str__(self):
    return f"{self.x} {self.y} {self.z}"

# class xyzclass:
#   def __init__(self,x:int,y:int,z:int):
#     self.x = x
#     self.y = y
#     self.z = z 

def norm(key):
  if isinstance(key, KeyCode) and key.char:
    return key.char.lower()
  return key

def on_press(key):
  k = norm(key)
  if k not in pressed:
    events.append(k)
  pressed.add(k)

def on_release(key):
  pressed.discard(norm(key))
  if key == Key.esc:
    return False

def handle_events():
  for ev in events:
    if ev == 'e':
      for px in pixels: px.x = -px.x
    elif ev == Key.alt_l or ev == Key.alt_r:
      for px in pixels: px.x, px.z = px.z, px.x
  events.clear()

def apply_held():
    """Движение по зажатым клавишам."""
    dx = dy = dz = 0
    if Key.up    in pressed or 'w' in pressed: dy += 1
    if Key.down  in pressed or 's' in pressed: dy -= 1
    if Key.left  in pressed or 'a' in pressed: dx -= 1
    if Key.right in pressed or 'd' in pressed: dx += 1
    if Key.shift_r in pressed:                 dz += 1
    if Key.shift_l in pressed:                 dz -= 1
    if dx or dy or dz:
        for px in pixels:
            px.x += dx
            px.y += dy
            px.z += dz

def DoFrame(pixels: list): # xyz: xyzclass
  symbols = [" ","█", "▓", "▒", "░", "≡", "=", "-", "."]
  Frame = CreateFrame(pixels, len(symbols))
  for i in reversed(range(len(Frame))):
    for j in range(len(Frame[i])):
      try:
        print(symbols[Frame[i][j]]*2, end="")
      except:
        pass
    print("")

def CreateFrame(pixels: list, len: int): # xyz: xyzclass
  a = create(15,15)
  Symbols_len = len-1
  for pix in pixels:
    z = pix.z
    if z > Symbols_len:
      z = Symbols_len
    
    try:
      a[pix.y][pix.x] = z
    except:
      pass
  return a

def create(lines: int, columns: int):
  a = []
  for _ in range(lines):
    line = []
    line += [0]*columns # " "
    a += [line] # or a.append(line)
  return a

def cybe(size: int):
  pixels = []
  for x in range(size):
    for y in range(size):
      px = pixel(x,y,1)
      pixels += [px]
  return pixels

def line(size: int):
  pixels = []
  for i in range(size):
    pixels += [pixel(i,i,i+1)]
  return pixels


# pixels = cybe(2) # cybe or line
# xyz = xyzclass(0,0,1)
# pixels = [pixel(2,3,1)]

if __name__ == "__main__":
    pixels = cybe(2)

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    try:
      while listener.running:
        handle_events()      # одноразовые действия
        apply_held()         # движение по зажатым

        sys.stdout.write("\033[H")
        DoFrame(pixels)
        sys.stdout.flush()

        time.sleep(1)
    finally:
      listener.stop()
# end = time.perf_counter()
# print(f"выполнилось за: {end - start:.6} секунд")

# pixels = []

# for el in pixels:
#   print(el)