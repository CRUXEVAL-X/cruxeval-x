from typing import Tuple

def f(key: str, value: str) -> Tuple[str, str]:
    """"""
    ### Canonical solution below ###
    dict_ = {key: value}
    return dict.popitem(dict_)

### Unit tests below ###
def check(candidate):
    assert candidate('read', 'Is') == ('read', 'Is')

def test_check():
    check(f)