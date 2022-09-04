queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

queries1 = {}

for query in queries:
    words = query.split()

    if len(words) in queries1.keys():
        queries1[len(words)] += 1
    else:
        queries1.update({len(words): 1})

for key, value in queries1.items():
    percentage = round((value / len(queries)) * 100, 2)
    print(f'Поисковых запросов из {key} слов: {percentage}% ({value} запр.)')