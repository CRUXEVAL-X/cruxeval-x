from typing import List

def f(text: List[str]) -> List[List[str]]:
    """"""
    ### Canonical solution below ###
    ls = []
    for x in text:
        ls.append(x.splitlines())
    return ls

### Unit tests below ###
def check(candidate):
    assert candidate(['Hello World\n"I am String"']) == [['Hello World', '"I am String"']]

def test_check():
    check(f)