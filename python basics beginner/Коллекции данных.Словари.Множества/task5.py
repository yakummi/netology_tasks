lst = ['2018-01-01', 'yandex', 'cpc', 100]
l = lst[-1]
for b in lst[-2::-1]:
    l = {b: l}
print(l)