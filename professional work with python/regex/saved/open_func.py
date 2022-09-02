import csv


def open_csv(csv_file: str):
    with open(csv_file, encoding='utf-8') as file:
        rows = csv.reader(file, delimiter=",")
        contacts_list = list(rows)

        return contacts_list


def writer_csv(result: list):
    # TODO 2: сохраните получившиеся данные в другой файл
    with open("phonebook.csv", "w", encoding='utf-8') as file:
        datawriter = csv.writer(file, delimiter=',')
        datawriter.writerows(result)