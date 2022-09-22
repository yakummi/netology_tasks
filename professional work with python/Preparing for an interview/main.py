brackets_example = '({[]})'
brackets_example2 = '{[]})'

class Stack:

    def __init__(self):
        self.brackets = []

    def is_Empty(self):
        if len(self.brackets) == 0:
            return True
        return False

    def push(self, new_el):
        self.brackets.append(new_el)

    def pop(self):
        return self.brackets.pop(-1)

    def peek(self):
        return self.brackets[-1]

    def size(self):
        return len(self.brackets)

    def check_verify(self, brackets_str):
        stack_brackets = [('(', ')'), ('[', ']'), ('{', '}')]
        if len(brackets_str) % 2 != 0:
            print('Несбалансировано')
            return False
        elif len(brackets_str) % 2 == 0:
            print('Сбалансировано')
            return True

        for verify in list(stack_brackets):
            for ver in brackets_str:
                if verify == ver[0]:
                    self.push(ver)
                elif verify == ver[1] and self.size() > 0 and self.pop() !=  ver[0]:
                    print('Несбалансировано')
                    return False
            brackets_str = brackets_str.replace(verify, '', 1)
            if self.is_Empty() and len(brackets_str) != 0:
                self.check_verify(brackets_str)
                return True
            elif self.is_Empty() and len(brackets_str) == 0:
                print('Сбалансировано')
                return True

if __name__ == '__main__':
    test = Stack()
    print(test.check_verify(brackets_example))
    print(test.check_verify(brackets_example2))