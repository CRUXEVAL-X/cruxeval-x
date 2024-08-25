from typing import List

def f(text: str, search_string: str) -> List[int]:
    """"""
    ### Canonical solution below ###
    indexes = []
    while search_string in text:
        indexes.append(text.rindex(search_string))
        text = text[:text.rindex(search_string)]
    return indexes

### Unit tests below ###
def check(candidate):
    assert candidate('ONBPICJOHRHDJOSNCPNJ9ONTHBQCJ', 'J') == [28, 19, 12, 6]

def test_check():
    check(f)