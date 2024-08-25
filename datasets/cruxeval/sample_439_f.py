def f(value: str) -> str:
    """"""
    ### Canonical solution below ###
    parts = value.partition(' ')[::2]
    return ''.join(parts)

### Unit tests below ###
def check(candidate):
    assert candidate('coscifysu') == 'coscifysu'

def test_check():
    check(f)