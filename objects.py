# objects

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

