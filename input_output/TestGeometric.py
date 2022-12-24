from Circle import Circle
from Retangle import Rectangle

circle = Circle(5)
circle.setColor("Green")
print(circle)
print("The circle radius :", circle.getRadius())
print("The circle area :", circle.getArea())
print(circle.printCircle())

rectangle = Rectangle(5, 10)
print("The rectangle perimeter :", rectangle.getPerimeter())
print("The rectangle area :", rectangle.getArea())
