from typing import Dict, Any, Union

def f(base: Dict[int, str], k: str, v: str) -> Dict[Union[str, int], str]:
    """"""
    ### Canonical solution below ###
    base[k] = v
    return base

### Unit tests below ###
def check(candidate):
    assert candidate({37: 'forty-five'}, '23', 'what?') == {37: 'forty-five', '23': 'what?'}

def test_check():
    check(f)