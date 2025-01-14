class Shape:
    def __init__(self, color):
        self.color = color


    def color(self):
        return self.color


class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height


    def perimeter(self):
        return 2 * self.width + self.height


    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius


    def perimeter(self):
        return 2 * self.radius + self.radius


    def area(self):
        return 2 * self.radius * self.radius


r = Rectangle(5, 7, 'Синий')
print(r.color)