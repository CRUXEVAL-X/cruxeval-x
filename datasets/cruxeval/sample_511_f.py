from typing import Tuple, Dict

def f(fields: Tuple[str, str, str], update_dict: Dict[str, str]) -> Dict[str, str]:
    """"""
    ### Canonical solution below ###
    di = dict((x, '') for x in fields)
    di.update(update_dict)
    return di

### Unit tests below ###
def check(candidate):
    assert candidate(('ct', 'c', 'ca'), {'ca': 'cx'}) == {'ct': '', 'c': '', 'ca': 'cx'}

def test_check():
    check(f)