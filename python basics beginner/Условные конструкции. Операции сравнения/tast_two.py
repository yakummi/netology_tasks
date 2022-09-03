class Zodiac:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def sing_zodiac(self):
        if self.month == 'Март' and 20 < self.day <= 31:
            return 'Овен'
        elif self.month == 'Апрель' and self.day <= 19:
            return 'Овен'
        elif self.month == 'Апрель' and 20 <= self.day <= 30:
            return 'Телец'
        elif self.month == 'Май' and self.day <= 20:
            return 'Телец'
        elif self.month == 'Май' and 21 <= self.day <= 31:
            return 'Близнецы'
        elif self.month == 'Июнь' and self.day <= 20:
            return 'Близнецы'
        elif self.month == 'Июнь' and 21 <= self.day <= 30:
            return 'Рак'
        elif self.month == 'Июль' and self.day <= 22:
            return 'Рак'
        elif self.month == 'Июль' and 23 <= self.day <= 31:
            return 'Лев'
        elif self.month == 'Август' and self.day <= 22:
            return 'Лев'
        elif self.month == 'Август' and 23 <= self.day <= 31:
            return 'Дева'
        elif self.month == 'Сентябрь' and self.day <= 22:
            return 'Дева'
        elif self.month == 'Сентябрь' and 23 <= self.day <= 30:
            return 'Весы'
        elif self.month == 'Октябрь' and self.day <= 22:
            return 'Весы'
        elif self.month == 'Октябрь' and 23 <= self.day <= 31:
            return 'Скорпион'
        elif self.month == 'Ноябрь' and self.day <= 21:
            return 'Скорпион'
        elif self.month == 'Ноябрь' and 22 <= self.day <= 30:
            return 'Стрелец'
        elif self.month == 'Декабрь' and self.day <= 21:
            return 'Стрелец'
        elif self.month == 'Декабрь' and 22 <= self.day <= 31:
            return 'Козерог'
        elif self.month == 'Январь' and self.day <= 19:
            return 'Козерог'
        elif self.month == 'Январь' and 20 <= self.day <= 31:
            return 'Водолей'
        elif self.month == 'Февраль' and self.day <= 19:
            return 'Водолей'
        elif self.month == 'Февраль' and 20 <= self.day <= 29:
            return 'Рыбы'
        elif self.month == 'Март' and self.day <= 19:
            return 'Рыбы'
month = input('Введите месяц: ')
day = int(input('Введите день: '))
my_date = Zodiac(month, day)
print(f'Вывод:\n{my_date.sing_zodiac()}')