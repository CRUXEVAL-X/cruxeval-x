from typing import List, Union

def f(array: List[int], const: int) -> List[str]:
    """"""
    ### Canonical solution below ###
    output = ['x']
    for i in range(1, len(array) + 1):
        if i % 2 != 0:
            output.append(str(array[i - 1] * -2))
        else:
            output.append(str(const))
    return output

### Unit tests below ###
def check(candidate):
    assert candidate([1, 2, 3], -1) == ['x', '-2', '-1', '-6']

def test_check():
    check(f)