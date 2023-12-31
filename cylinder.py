import math

class Cylinder:

  def __init__(self, height=1, radius=1): 
    self.height = height
    self.radius = radius

  def volume(self): 
    return math.pi * self.height * (self.radius**2)
    
  def surface_area(self):
    return 2 * math.pi * self.radius * (self.height + self.radius)

C = Cylinder(2,3)


print("Volume ",C.volume())
print("Surface Area ",C.surface_area())
