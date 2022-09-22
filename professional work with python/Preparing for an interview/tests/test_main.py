import pytest
from main import Stack

test_data = [
    ('{((((([])))))}[]', True),
    ('((()){{{]]', False),
    ('((){}[]))', False),
    ('({[({[([{}])]})]})', True),
    ('((()){{{]]', False),
    ('({{{}}}((()))[[[]]])', True),
    ('({[]})', True)
]

test_obg = Stack()

@pytest.mark.parametrize('test_list, result', test_data)
def test_main_func(test_list, result):
    check_result = test_obg.check_verify(test_data)
    assert check_result == result
