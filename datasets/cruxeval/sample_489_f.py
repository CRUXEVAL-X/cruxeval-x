def f(text: str, value: str) -> str:
    """"""
    ### Canonical solution below ###
    return text.removeprefix(value.lower())

### Unit tests below ###
def check(candidate):
    assert candidate('coscifysu', 'cos') == 'cifysu'

def test_check():
    check(f)