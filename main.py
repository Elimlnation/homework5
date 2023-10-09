# first way
# import math
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# class Circle:
#     def __init__(self, x, y, radius):
#         self.center = Point(x, y)
#         self.radius = radius
#
#     def contains(self, point):
#         distance = math.sqrt((point.x - self.center.x)**2 + (point.y - self.center.y)**2)
#         return distance <= self.radius
#
# circle = Circle(0, 0, 5)
# point_inside = Point(3, 4)
# point_outside = Point(6, 6)
#
# print(circle.contains(point_inside))
# print(circle.contains(point_outside))
# second way
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, x, y, radius):
        self.center = Point(x, y)
        self.radius = radius

    def contains(self, point):
        distance = math.sqrt((point.x - self.center.x)**2 + (point.y - self.center.y)**2)
        return distance <= self.radius

x_center = float(input("Enter the X-coordinate of the circle's center: "))
y_center = float(input("Enter the Y-coordinate of the circle's center: "))
radius = float(input('Enter the radius of the circle: '))

circle = Circle(x_center, y_center, radius)

x_point = float(input('Enter the X-coordinate of the point: '))
y_point = float(input('Enter the Y-coordinate of the point: '))

point = Point(x_point, y_point)

if circle.contains(point):
    print('The point is inside the circle.')
else:
    print('The point is outside the circle.')
