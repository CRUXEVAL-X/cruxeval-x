from typing import List

def f(names: List[str]) -> int:
    """"""
    ### Canonical solution below ###
    count = len(names)
    numberOfNames = 0
    for i in names:
        if i.isalpha():
            numberOfNames += 1
    return numberOfNames

### Unit tests below ###
def check(candidate):
    assert candidate(['sharron', 'Savannah', 'Mike Cherokee']) == 2

def test_check():
    check(f)