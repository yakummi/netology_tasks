documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

list_commands = ['p', 's', 'l', 'a']

class Choice:
    def __init__(self, command):
        self.command = command

    def polka(self):
        if self.command == 'p':
            number_doc = input('Введите номер документа: ')
            for i in documents:
                if i['number'] == number_doc:
                    print(i)
                else:
                    print('Человек с таким документом не найден.')
        if self.command == 's':
            number_doc = input('Введите номер документа: ')
            for k, v in directories.items():
                if number_doc in v:
                    print(f'Документ {number_doc} находится на {k} полке.')
                else:
                    print('Документ не найден.')
        if self.command == 'l':
            for i in documents:
                for v in i.values():
                    print(v)

        if self.command == 'a':
            nomer = input('Введите ваш номер: ')
            tip = input('Введите тип: ')
            name = input('Введите ваше имя: ')
            polka = input('Введите полку, на которую хотите отправить ваш документ: ')
            doc = {'type': tip, 'number': nomer, 'name': name}
            documents.append(doc)
            directories[polka].append(doc['number'])
            return 'Документ добавлен'

