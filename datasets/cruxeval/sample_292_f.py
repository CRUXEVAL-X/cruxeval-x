def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    new_text = [c if c.isdigit() else '*' for c in text]
    return ''.join(new_text)

### Unit tests below ###
def check(candidate):
    assert candidate('5f83u23saa') == '5*83*23***'

def test_check():
    check(f)