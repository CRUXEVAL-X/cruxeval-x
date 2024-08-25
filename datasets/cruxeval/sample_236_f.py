from typing import List

def f(array: List[str]) -> str:
    """"""
    ### Canonical solution below ###
    if len(array) == 1:
        return ''.join(array)
    result = list(array)
    i = 0
    while i < len(array)-1:
        for j in range(2):
            result[i*2] = array[i]
            i += 1
    return ''.join(result)

### Unit tests below ###
def check(candidate):
    assert candidate(['ac8', 'qk6', '9wg']) == 'ac8qk6qk6'

def test_check():
    check(f)