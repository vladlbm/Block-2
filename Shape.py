import math


class Shape:
    def __init__(self, name):
        self.name = name


    def area(self):
        """Переопределяющий метод для вычисления площади в других подклассах """
        raise NotImplementedError(f'Метод area требует определения в классе: {self.__class__.__name__}')


    def name_info(self):
        print(f'Фигура: {self.name}')


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__('Rectangle')
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Circle')
        self.radius = radius


    def area(self):
        return math.pi * (self.radius ** 2)



