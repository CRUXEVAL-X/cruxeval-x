from typing import List

def f(matrix: List[List[int]]) -> List[List[int]]:
    """"""
    ### Canonical solution below ###
    matrix.reverse()
    result = []
    for primary in matrix:
        max(primary)
        primary.sort(reverse = True)
        result.append(primary)
    return result

### Unit tests below ###
def check(candidate):
    assert candidate([[1, 1, 1, 1]]) == [[1, 1, 1, 1]]

def test_check():
    check(f)