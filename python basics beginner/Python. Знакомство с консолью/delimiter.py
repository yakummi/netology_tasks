# Заработок в месяц
# Ипотека в месяц / переменная в год
# ЛЖ в месяц / переменная в год
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

print('#' * int(z * z + (x+x+y+y)))


def main():
    salary_month = float(input('Введите ваш заработок в месяц: '))
    ipoteka_month = float(input('Введите ипотеку за месяц: '))
    IPOTEKA = salary_month * ipoteka_month / 100 # Формула для ипотеки
    life_month = float(input('Введите сколько вы тратите на личную жизнь: '))
    LIFE = salary_month * life_month / 100
    FINISH_NAL = (salary_month * 12) - (IPOTEKA * 12 + LIFE * 12)
    print(f'Было накоплено: {FINISH_NAL}')
    print(f'Потрачено на ипотеку: {IPOTEKA * 12}')
main()