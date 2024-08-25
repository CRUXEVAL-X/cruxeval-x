def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    return text.replace('\\"', '"')

### Unit tests below ###
def check(candidate):
    assert candidate('Because it intrigues them') == 'Because it intrigues them'

def test_check():
    check(f)