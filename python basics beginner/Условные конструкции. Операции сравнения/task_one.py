import sys

regions = ['Республика Бурятия', 'Республика Саха', 'Забайкальский край', 'Камчатский край', 'Приморский край',
           'Хабаровский край', 'Амурская область', 'Магаданская область', 'Сахалинская область',
           'Еврейская автономная область', 'Чукотский автономный округ'] # регионы Дальнего востока

base_bet = 10

region = input('Введите ваш регион: ')
if region in regions:
    print(f'Ваша процентная ставка -> {base_bet - 2}%')
    sys.exit()

kids = int(input('Введите кол-во детей: '))
if kids > 3:
    base_bet = base_bet - 1

project = input('Есть ли у вас зарплатный проект в нашем банке? Да|Нет: ')
if project == 'Да':
    base_bet = base_bet - 0.5

save_bet = input('Будете ли вы оформлять страхование в нашем банке? Да|Нет: ')
if save_bet == 'Да':
    base_bet = base_bet - 1.5

print(f'{base_bet}%')