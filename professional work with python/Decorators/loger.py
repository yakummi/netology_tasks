import datetime
import os

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

def loger(path):
    def loger_(some_function):
        def new_function(*args, **kwargs):
            date = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")
            name = some_function.__name__
            args_ = args
            result = some_function(*args, **kwargs)
            with open(path + '/time.txt', 'a') as file:
                file.write(f'{date} | {name} | {args_} | {result}\n')
            return result
        return new_function
    return loger_

PATH = os.path.dirname(os.path.realpath(__file__))

@loger(PATH)
def recurse(arr):
    for item in arr:
        if isinstance(item, list):
            yield from recurse(item)
        else:
            yield item

if __name__ == '__main__':
    for item in recurse(nested_list):
        print(item)
