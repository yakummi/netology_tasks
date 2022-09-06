import csv
import re
from pprint import pprint


def reader():
    with open('phonebook_raw.csv', encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=',')
        contacts_list = list(rows)
    return contacts_list


def split_names(some_list):
    for i in some_list:
        for j in i[:3]:
            a = j.split()
            if len(a) == 1:
                continue
            elif len(a) == 2:
                i[0] = a[0]
                i[1] = a[1]
            elif len(a) == 3:
                i[0] = a[0]
                i[1] = a[1]
                i[2] = a[2]
    return some_list


def duplicate_deleting(new_list):
    some_list = [new_list[0]]
    for i in new_list[1:]:
        if i[0] not in [j[0] for j in some_list]:
            some_list.append(i)
        else:
            for j in some_list:
                if j[0] == i[0]:
                    j.extend([k for k in i if k not in j])
    return some_list


def phone_editor(some_list: list) -> list:
    pattern = r'(\+7|8)\s*?\(?(\d{3})\)?\s*?-?\s*(\d{3})-?(\d{2})-?(\d{2})\s*\(?(доб.\s*\d*)?\)?'
    substitution = r'+7(\2)-\3-\4-\5 \6'
    new_list = []
    for item in some_list:
        text = ' '.join(i for i in item)
        new = re.sub(pattern, substitution, text)
        new_list.append([new])
    return new_list


def writer(some_list):
    with open('phonebook.csv', 'w', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(some_list)