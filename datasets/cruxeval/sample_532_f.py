from typing import List

def f(n: int, array: List[int]) -> List[List[int]]:
    """"""
    ### Canonical solution below ###
    final = [array.copy()] 
    for i in range(n):
        arr = array.copy()
        arr.extend(final[-1])
        final.append(arr)
    return final

### Unit tests below ###
def check(candidate):
    assert candidate(1, [1, 2, 3]) == [[1, 2, 3], [1, 2, 3, 1, 2, 3]]

def test_check():
    check(f)