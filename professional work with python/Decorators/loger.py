import datetime

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

def loger():
    def loger_(some):
        def writer(*args, **kwargs):
            date = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")
            name = some.__name__
            args_ = args
            result = some(*args, **kwargs)
            with open('time.txt', 'w', encoding='utf-8') as f:
                f.write(f'{date} | {name} | {args_} | {result}\n')
            return result
        return writer
    return loger_


@loger()
def recurse(arr):
    for item in arr:
        if isinstance(item, list):
            yield from recurse(item)
        else:
            yield item

if __name__ == '__main__':
    for item in recurse(nested_list):
        print(item)