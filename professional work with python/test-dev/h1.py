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

def main_help():
    help_menu = [
        "help - список команд",
        "p - выводит имя человека, на которого оформлен документ",
        "s - выводит номер полки архива, на которой хранится документ",
        "l - выводит список всех документов в каталоге",
        "a - добавляет новый документ в каталог и на полку архива",
        "d - удаляет документ из каталога и архива",
        "m - переносит документ на указанную полку архива",
        "as - добавляет новую полку в архив",
        "q - выход"
    ]
    for commands in help_menu:
        print(commands)

def document_owner(docs: list) -> str:
        number = input('Введите номер документа: ')
        for num in docs:
            if num['number'] == number:
                return f"Владелец документа - {num['name']}"
        return 'Документ отсутствует.'

def documents_in_shelf(dirs: dict) -> str:
    number = input('Введите номер документа: ')
    for k, v in dirs.items():
        if number in v:
            return f"Документ на полке - {k}"
    return 'Документ отсутствует.'

def general_docs(docs: list) -> list:
    share_list = []
    for elements in docs:
        share_list.append(list(elements.values()))
    return share_list

def new_documents_for_add(doc_type, doc_number, doc_person):
    new_doc = {
        'type': doc_type,
        'number': doc_number,
        'person': doc_person
    }
    return new_doc

def add_documents(docs: list, dirs: dict, new_document: dict) -> str:
    shelf_number = input('Введите номер полки: ')
    for num in docs:
        if num['number'] == new_document['number']:
            return 'Документ уже существует.'
    if shelf_number in dirs.keys():
        docs.append(new_document)
        dirs[shelf_number].append(new_document['number'])
        return 'Документ успешно добавлен.'
    return 'Номер полки не существует.'

def delete_documents(docs, dirs):
    number_document = input('Введите номер документа: ')
    if any(number_document in shelf for shelf in dirs.values()):
        for k in dirs.keys():
            if number_document in dirs[k]:
                dirs[k].remove(number_document)
        for doc in docs:
            if doc['number'] == number_document:
                docs.remove(doc)
        return 'Удаление прошло успешно.'
    return 'Документ отсутствует.'

def moving_documents(docs, dirs):
    number_doc = input('Введите номер документа: ')
    number_shelf = input('Введите номер полки: ')
    if number_shelf not in dirs.keys():
        return 'Номер полки не существует.'
    elif not any(number_doc in shelf for shelf in dirs.values()):
        return 'Документ отсутствует.'
    else:
        for k in dirs.keys():
            if number_doc in dirs[k]:
                dirs[k].remove(number_doc)
                dirs[number_shelf].append(number_doc)
            return 'Документ перемещен на указанную полку.'

def new_shelf(dirs):
    number_shelf = input('Введите номер полки: ')
    if number_shelf in dirs.keys():
        return 'Полка уже существует.'
    dirs.setdefault(number_shelf, [])
    return 'Полка успешно добавлена.'


def main():
    print('help - список команд\nq - выход')

    while True:
        command = input('Введите команду: ')
        if command == 'p':
            print(f'\n{document_owner(documents)}')
        elif command == 's':
            print(f'\n{documents_in_shelf(directories)}')
        elif command == 'l':
            print(general_docs(documents))
        elif command == 'a':
            type_ = input('Введите тип документа: ')
            number = input('Введите номер документа: ')
            name = input('Введите имя владельца: ')
            new_doc = new_documents_for_add(type_, number, name)
            print(f'\n{add_documents(documents, directories, new_doc)}')
        elif command == 'd':
            print(f'\n{delete_documents(documents, directories)}')
        elif command == 'm':
            print(f'\n{moving_documents(documents, directories)}')
        elif command == 'as':
            print(f'\n{new_shelf(directories)}')
        elif command == 'help':
            main_help()
        elif command == 'q':
            return 'Выход'

if __name__ == '__main__':
    print(main())
