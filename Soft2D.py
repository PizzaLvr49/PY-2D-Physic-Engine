import time
import logging
import math
import turtle

class Vector2:
    
    def __init__(self, X: float, Y: float) -> None:
        self.x = X
        self.y = Y
        
    def magnitude(self):
        
        return math.sqrt( self.x^2 + self.y^2)
        
    def unit(self):
        
        return Vector2(self.x / self.magnitude(), self.y / self.magnitude())
        
    def __add__(self, other):
        if other.__class__ == self.__class__:
            
            return Vector2(self.x + other.x, self.y + other.y)
        
        elif ValueError:
            logging.error("Must be Vector2")
            NotImplemented
            
    def __mul__ (self, other):
        if other.__class__ == self.__class__:
            
            return Vector2(self.x * other.x, self.y * other.y)
        
        elif type(other) is float or type(other) is int:
            return Vector2(self.x * other, self.y * other)
        elif ValueError:
            logging.error("ValueError: must be float or Vector2")
            NotImplemented
    
    def __rmul__(self, other):
        if other.__class__ == self.__class__:
            
            return Vector2(self.x * other.x, self.y * other.y)
        
        elif type(other) is float or type(other) is int:
            return Vector2(self.x * other, self.y * other)
        elif ValueError:
            logging.error("ValueError: must be float or Vector2")
            NotImplemented
    
    def __repr__(self) -> str:
        return "X:" + str(self.x) + " Y:" + str(self.y)
    
class MassPoint:
    
    def __init__(self, pos: Vector2 , mass):
        self.pos = pos
        self.velocity = Vector2(0,0)
        self.Mass = mass
        
    def __repr__(self) -> str:
        return "X:" + str(self.pos.x) + " Y:" + str(self.pos.y) + " Mass:" + str(self.Mass)
    
    def ApplyForce(self, dir: Vector2, force: float):
        
        unit_dir = dir.unit()
        
        self.velocity += unit_dir * force
    
    def tick(self):
        self.pos += self.velocity
        self.velocity *= 0.9


point1 = MassPoint(Vector2(5, 5), 55)

print(point1)

point1.ApplyForce(Vector2(5, 50), 5)

print(point1.velocity)

while True:
    point1.tick()
    time.sleep(0.1)
    print(point1.pos)