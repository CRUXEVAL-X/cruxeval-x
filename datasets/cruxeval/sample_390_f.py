def f(text: str) -> int:
    """"""
    ### Canonical solution below ###
    if not text.strip():
        return len(text.strip())
    return None

### Unit tests below ###
def check(candidate):
    assert candidate(" \t ") == 0

def test_check():
    check(f)