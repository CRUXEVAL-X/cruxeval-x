from typing import List

def f(array: List[int]) -> List[str]:
    """"""
    ### Canonical solution below ###
    just_ns = list(map(lambda num: 'n'*num, array))
    final_output = []
    for wipe in just_ns:
        final_output.append(wipe)
    return final_output

### Unit tests below ###
def check(candidate):
    assert candidate([]) == []

def test_check():
    check(f)