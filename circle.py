import math

class Circle:
  def __init__(self, radius) -> None:
    self.radius = radius

  @property
  def area(self):
    return math.pi * self.radius ** 2
