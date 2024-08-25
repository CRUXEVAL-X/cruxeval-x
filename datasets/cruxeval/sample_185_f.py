from typing import List

def f(L: List[int]) -> List[int]:
    """"""
    ### Canonical solution below ###
    N = len(L)
    for k in range(1, N//2 + 1):
        i = k - 1
        j = N - k
        while i < j:
            # swap elements:
            L[i], L[j] = L[j], L[i]
            # update i, j:
            i += 1
            j -= 1
    return L

### Unit tests below ###
def check(candidate):
    assert candidate([16, 14, 12, 7, 9, 11]) == [11, 14, 7, 12, 9, 16]

def test_check():
    check(f)