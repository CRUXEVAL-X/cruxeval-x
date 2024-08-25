from typing import List

def f() -> List[str]:
    """"""
    ### Canonical solution below ###
    d = {
        'Russia': [('Moscow', 'Russia'), ('Vladivostok', 'Russia')],
        'Kazakhstan': [('Astana', 'Kazakhstan')],
    }
    return list(d.keys())

### Unit tests below ###
def check(candidate):
    assert candidate() == ['Russia', 'Kazakhstan']

def test_check():
    check(f)