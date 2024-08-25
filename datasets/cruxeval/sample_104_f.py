from typing import Dict

def f(text: str) -> Dict[str, int]:
    """"""
    ### Canonical solution below ###
    dic = dict()
    for char in text:
        dic[char] = dic.get(char, 0) + 1
    for key in dic:
        if dic[key] > 1:
            dic[key] = 1
    return dic

### Unit tests below ###
def check(candidate):
    assert candidate("a") == {'a': 1}

def test_check():
    check(f)