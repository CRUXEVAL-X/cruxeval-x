def f(text: str, value: str) -> int:
    """"""
    ### Canonical solution below ###
    if isinstance(value, str):
        return text.count(value) + text.count(value.lower())
    return text.count(value)

### Unit tests below ###
def check(candidate):
    assert candidate('eftw{ьТсk_1', '\\') == 0

def test_check():
    check(f)