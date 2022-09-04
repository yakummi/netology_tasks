ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
digits = []
new_ids = list(ids)
i = 1
for e in new_ids:
    print(ids[f'user{i}'])
    for element in ids[f'user{i}']:
        if element not in digits:
            digits.append(element)
    i += 1
print(digits)