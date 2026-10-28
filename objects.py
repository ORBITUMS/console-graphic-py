# objects
import math

class pixel:
  def __init__(self,x:int,y:int,z:int):
    self.x = x
    self.y = y
    self.z = z 
  
  def __str__(self):
    return f"{self.x} {self.y} {self.z}"

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

def rcybe(size: int):
  pixels = []
  for i in range(size):
    px = pixel(i+3,4,2)
    pixels += [px]
  return pixels

def ventilator(size: int):
  pixels = []
  for i in range(size):
    px = pixel(4,i+2,1)
    pixels += [px]
  return pixels

def VentRot(pixels: list):
  i = 1
  max1 = 0
  max2 = 0
  for i in range(len(pixels)):
    if pixels[i].y > pixels[max1].y and pixels[i].x == pixels[max1].x:
      max2 = max1
      max1 = i

  pixels[max1].x =+1
  return pixels
  
