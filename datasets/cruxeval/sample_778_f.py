def f(prefix: str, text: str) -> str:
    """"""
    ### Canonical solution below ###
    if text.startswith(prefix):
        return text
    else:
        return prefix + text

### Unit tests below ###
def check(candidate):
    assert candidate('mjs', 'mjqwmjsqjwisojqwiso') == 'mjsmjqwmjsqjwisojqwiso'

def test_check():
    check(f)