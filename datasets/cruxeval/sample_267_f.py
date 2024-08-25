def f(text: str, space: int) -> str:
    """"""
    ### Canonical solution below ###
    if space < 0:
        return text
    return text.ljust(len(text) // 2 + space)

### Unit tests below ###
def check(candidate):
    assert candidate('sowpf', -7) == 'sowpf'

def test_check():
    check(f)