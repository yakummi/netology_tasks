def main():
    salary_month = float(input('Введите ваш заработок в месяц: '))
    ipoteka_month = float(input('Введите ипотеку за месяц: '))
    IPOTEKA = salary_month * ipoteka_month / 100 # Формула для ипотеки
    life_month = float(input('Введите сколько вы тратите на личную жизнь: '))
    LIFE = salary_month * life_month / 100
    FINISH_NAL = (salary_month * 12) - (IPOTEKA * 12 + LIFE * 12)
    return(f'Было накоплено: {FINISH_NAL}') /
        f'Потрачено на ипотеку: {IPOTEKA * 12}'
if __name__ == '__main__':
    main()