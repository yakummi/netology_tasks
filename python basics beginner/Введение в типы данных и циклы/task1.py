boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    boys.sort()
    girls.sort()
    finish = list(zip(boys, girls))
    for f in finish:
        print(f)
else:
    print('Кому-то не нашлась пара')