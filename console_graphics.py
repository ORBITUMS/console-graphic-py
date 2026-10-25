# import time
# start = time.perf_counter()

# сделать потом вращяющяюся шнягу какую-нибудь
from pynput import keyboard
from pynput.keyboard import Key, KeyCode

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

def on_press(key):
  global pixels

  if key == Key.up:
    for px in pixels: px.y += 1
    DoFrame(pixels)
  elif key == Key.down:
    for px in pixels: px.y -= 1
    DoFrame(pixels)
  elif key == Key.left:
    for px in pixels: px.x -= 1
    DoFrame(pixels)
  elif key == Key.right:
    for px in pixels: px.x += 1
    DoFrame(pixels)
  elif key == Key.shift_r:
    for px in pixels: px.z += 1
    DoFrame(pixels)
  elif key == Key.shift_l:
    for px in pixels: px.z -= 1
    DoFrame(pixels)
  elif key == Key.alt_r:
    for px in pixels:
      px.x, px.z = px.z, px.x
    DoFrame(pixels)
  elif key == Key.alt_l:
    for px in pixels:
      px.x, px.z = px.z, px.x
    DoFrame(pixels)
  elif key == Key.esc:
      return False

  elif isinstance(key, KeyCode) and key.char:
    ch = key.char.lower()  
    if ch == 'w':
      for px in pixels: px.y += 1 
      DoFrame(pixels)
    elif ch == 's':
      for px in pixels: px.y -= 1 
      DoFrame(pixels)
    elif ch == 'a':
      for px in pixels: px.x -= 1  
      DoFrame(pixels)
    elif ch == 'd':
      for px in pixels: px.x += 1 
      DoFrame(pixels)
    elif ch == 'q':
      for px in pixels: px.y -= 1 
      DoFrame(pixels)
    elif ch == 'e':
      for px in pixels: px.x = -px.x 
      DoFrame(pixels)
    else:
      return
  else:
    return

if __name__ == "__main__":
  pixels = cybe(2) # cybe or line
  # xyz = xyzclass(0,0,1)
  # pixels = [pixel(2,3,1)]

  DoFrame(pixels) #xyz
  with keyboard.Listener(on_press=on_press) as listener:
    listener.join()



# end = time.perf_counter()
# print(f"выполнилось за: {end - start:.6} секунд")

# pixels = []

# for el in pixels:
#   print(el)