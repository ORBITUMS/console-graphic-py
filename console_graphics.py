# main

import time
import sys

from pynput import keyboard
from pynput.keyboard import Key, KeyCode

import objects as obj
import editor as ed

actions = [] # все действия за текущий кадр

def norm(key):
  if isinstance(key, KeyCode) and key.char:
    return key.char.lower()
  return key

def on_press(key):
  k = norm(key)
  actions.append(k)

def on_release(key):
  if key == Key.esc:
    return False

def process_actions():
  global actions
  for ev in actions:
    if ev == Key.up    or ev == 'w': 
      for px in pixels: px.z -= 1
    elif ev == Key.down  or ev == 's': 
      for px in pixels: px.z += 1
    elif ev == Key.left  or ev == 'a': 
      for px in pixels: px.x += 1
    elif ev == Key.right or ev == 'd': 
      for px in pixels: px.x -= 1
    elif ev == Key.shift_r or ev == "e": 
      for px in pixels:
        x,z = px.x, px.z  
        px.z,px.x = x,-z
        
    elif ev == Key.shift_l or ev == "q": 
      for px in pixels:
        x,z = px.x, px.z  
        px.z,px.x = -x,z

    #elif ev == Key.alt_l or ev == Key.alt_r:
    #  for px in pixels: px.x, px.z = px.z, px.x

  actions.clear()

def DoFrame(pixels: list): # xyz: xyzclass
  symbols = ["/","█", "▓", "▒", "░", "≡", "=", "-", "."," "]
  Frame = CreateFrame(pixels, len(symbols))
  Buf_Frame = ""
  lines = []
  for y in reversed(range(len(Frame))):
    for x in range(len(Frame[y])):
      try:
        Buf_Frame += symbols[Frame[y][x]]*2
        # Buf_Frame += str(Frame[y][x])
      except:
        pass
    lines += [Buf_Frame]
    Buf_Frame = ""
    #print(Frame[i][j], end="")
  sys.stdout.write("\033[H" + "\n".join(lines) + "\n")
  sys.stdout.flush()

def CreateFrame(pixels: list, symbol_count: int): # xyz: xyzclass
  global TFS, fog
  Symbols_len = symbol_count-1
  A = [[Symbols_len]*TFS for _ in range(TFS)] # [[0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
  TFS = TFS
  half = TFS//2
  for pix in pixels:
    z = pix.z
    if not fog > z:
      continue
    elif Symbols_len-1 < z:
      z = Symbols_len-1
      
    #if 0 <= z: # if camera.z <= z:
    x = pix.x + half
    y = pix.y + half
    if x >= 0 and x < TFS and y >= 0 and y < TFS and z >= 0:
      if A[y][x] > z:
        A[y][x] = z
  return A

# xyz = xyzclass(0,0,1)
# pixels = [pixel(2,3,1)]
def start():
    global TFS, fog, FPS, pixels, camera
    settings = bool(input("start game 1 - yes, 0 - settings: "))

    if settings:
      TFS = int(input("20: "))  # TerminalFrameSize
      fog = int(input("Fog: "))
      FPS = int(input("FPS: "))
    else:
      TFS = 24
      fog = 20
      FPS = 10

    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    pixels = ed.pixels         # obj.map(6) cybe or line or map( size === 0 mod 2)
    camera = obj.pixel(0, 0, 0)

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    try:
        while listener.running:
            time.sleep(1/FPS)
            process_actions()
            # pixels = obj.VentRot(pixels)
            sys.stdout.write("\033[H")
            DoFrame(pixels)
            sys.stdout.flush()
    finally:
        listener.stop()
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()
        print("")
        print("Вы вышли из цикла.", end="\n\n\n")


if __name__ == "__main__":
    start()

# pixels = []
# for el in pixels:
#   print(el)