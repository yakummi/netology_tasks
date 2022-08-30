# Пользователь вводит длину и ширину фигуры.
# Программа выводит их периметр и площадь.
z = float(input('Введите сторону квадрата: '))
class Square:
    def __init__(self, z):
        self.z = z

    def perimeter(self):
        return f'Периметр: {self.z * 4}'

    def square(self):
        return f'Площадь: {self.z * self.z}'

test1 = Square(z)
print(test1.perimeter())
print(test1.square())

x = float(input('Введите длину: '))
y = float(input('Введите ширину: '))
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def perimeter(self):
        return f'Периметр: {self.x * 2 + self.y * 2}'

    def square(self):
        return f'Площадь: {self.x * self.y}'

test = Rectangle(x, y)
print(test.perimeter())
print(test.square())