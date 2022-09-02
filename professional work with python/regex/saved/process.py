import regex as re

def change_name(text, pattern):
    for employee in text:
        lst = list(filter(None, [*pattern.split(employee[0]), *pattern.split(employee[1])]))
        if len(lst) == 3:
            employee[0], employee[1], employee[2] = lst[0], lst[1], lst[2]
        elif len(lst) == 2:
            employee[0], employee[1] = lst[0], lst[1]
        else:
            employee[0] = lst[0]


def change_number(text, pattern, subs):
    for employee in text:
        employee[5] = re.sub(pattern, subs, employee[5]).strip(' ')


def finish(table):
    result_table = []
    group_list = []
    for key in table:
        if key[0:2] not in result_table:
            result_table.append(key[0:2])
            group_list.append([key[2:]])
        else:
            count = result_table.index(key[0:2])
            group_list[count].append(key[2:])

    for i, element in enumerate(group_list):
        if len(element) > 1:
            concat = list(zip(element[0], element[1]))
            for j, elem in enumerate(concat):
                if elem[0] == elem[1]:
                    concat[j] = elem[0]
                elif elem[0] == "":
                    concat[j] = elem[1]
                elif elem[1] == "":
                    concat[j] = elem[0]
            group_list[i] = concat
        else:
            group_list[i] = [item for i in element for item in i]

    for i, name in enumerate(result_table):
        result_table[i] = name + group_list[i]

    return result_table