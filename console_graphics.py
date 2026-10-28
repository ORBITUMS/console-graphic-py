# main

import time
import sys

from pynput import keyboard
from pynput.keyboard import Key, KeyCode

import objects as obj


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
      for px in pixels: px.y += 1
    elif ev == Key.down  or ev == 's': 
      for px in pixels: px.y -= 1
    elif ev == Key.left  or ev == 'a': 
      for px in pixels: px.x -= 1
    elif ev == Key.right or ev == 'd': 
      for px in pixels: px.x += 1
    elif ev == Key.shift_r: 
      for px in pixels: px.z += 1
    elif ev == Key.shift_l: 
      for px in pixels: px.z -= 1

    elif ev == Key.alt_l or ev == Key.alt_r:
      for px in pixels: px.x, px.z = px.z, px.x

  actions.clear()

def DoFrame(pixels: list): # xyz: xyzclass
  symbols = [" ","█", "▓", "▒", "░", "≡", "=", "-", "."]
  Frame = CreateFrame(pixels, len(symbols))
  for i in reversed(range(len(Frame))):
    for j in range(len(Frame[i])):
      try:
        print(symbols[Frame[i][j]]*2, end="")
        # print(Frame[i][j], end="")
      except:
        pass
    print("")

def CreateFrame(pixels: list, len: int): # xyz: xyzclass
  global TerminalFrameSize
  a = create(TerminalFrameSize,TerminalFrameSize)
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


# xyz = xyzclass(0,0,1)
# pixels = [pixel(2,3,1)]

if __name__ == "__main__":
  TerminalFrameSize = 30


  sys.stdout.write("\033[2J\033[H")
  sys.stdout.flush()
  pixels = obj.ventilator(5) # cybe or line


  listener = keyboard.Listener(on_press=on_press, on_release=on_release)
  listener.start()

  try:
    while listener.running:
      time.sleep(1/10)
      process_actions()
      pixels = obj.VentRot(pixels)
      sys.stdout.write("\033[H")
      DoFrame(pixels)
      sys.stdout.flush()

  finally:
    listener.stop()
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()
    print("")
    print("Вы вышли из цикла.", end="\n\n\n")



# pixels = []
# for el in pixels:
#   print(el)