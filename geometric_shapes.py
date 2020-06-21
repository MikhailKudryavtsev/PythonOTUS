import math


class GeometricShapes:

    def calculate_the_area(self, name, a, h, b, r):
        if name == 'Triangle':
            self.area = int(1 / 2 * a * h)
        elif name == 'Square':
            self.area = int(a ** 2)
        elif name == 'Rectangle':
            self.area = int(a * b)
        elif name == 'Circle':
            self.area = int(math.pi * (r ** 2))
        print(f'\nПлощадь фигуры {name} равна {self.area}')
        return self.area

    def calculate_perimeter(self, name, a, b, c, r):
        if name == 'Triangle':
            self.perimeter = int(a + b + c)
        elif name == 'Square':
            self.perimeter = int(4 * a)
        elif name == 'Rectangle':
            self.perimeter = int(2 * (a + b))
        elif name == 'Circle':
            self.perimeter = int(2 * math.pi * r)
        print(f'\nПериметр фигуры {name} равен {self.perimeter}')
        return self.perimeter

    class Circle:
        name = 'Circle'
        angles = 0
        perimeter = 0
        area = 0

        @staticmethod
        def add_square(a, h, b, r, figure2):
            try:
                sum_area = GeometricShapes().calculate_the_area(
                    name=GeometricShapes.Circle.name, a=a, h=h, b=b, r=r) + figure2
                print(f'\nСумма площадей = {sum_area}')
                return sum_area
            except TypeError:
                print(f'\nОшибка. {figure2} не геометическая фигура.')
                return False

    class Triangle:
        name = 'Triangle'
        angles = 3
        perimeter = 0
        area = 0

        @staticmethod
        def add_square(a, h, b, r, figure2):
            try:
                sum_area = GeometricShapes().calculate_the_area(
                    name=GeometricShapes.Triangle.name, a=a, h=h, b=b, r=r) + figure2
                print(f'\nСумма площадей = {sum_area}')
                return sum_area
            except TypeError:
                print(f'\nОшибка. {figure2} не геометическая фигура.')
                return False

    class Rectangle:
        name = 'Rectangle'
        angles = 4
        perimeter = 0
        area = 0

        @staticmethod
        def add_square(a, h, b, r, figure2):
            try:
                sum_area = GeometricShapes().calculate_the_area(
                    name=GeometricShapes.Rectangle.name, a=a, h=h, b=b, r=r) + figure2
                print(f'\nСумма площадей = {sum_area}')
                return sum_area
            except TypeError:
                print(f'\nОшибка. {figure2} не геометическая фигура.')
                return False

    class Square:
        name = 'Square'
        area = 0
        angles = 4
        perimeter = 0

        @staticmethod
        def add_square(a, h, b, r, figure2):
            try:
                sum_area = GeometricShapes().calculate_the_area(
                    name=GeometricShapes.Square.name, a=a, h=h, b=b, r=r) + figure2
                print(f'\nСумма площадей = {sum_area}')
                return sum_area
            except TypeError:
                print(f'\nОшибка. {figure2} не геометическая фигура.')
                return False
