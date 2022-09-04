stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
lst = [a for a, b in stats.items()
       if b == max(stats.values())]
print(lst)