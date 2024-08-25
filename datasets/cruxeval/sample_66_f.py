def f(text: str, prefix: str) -> str:
    """"""
    ### Canonical solution below ###
    prefix_length = len(prefix)
    if text.startswith(prefix):
        return text[(prefix_length - 1) // 2:
                    (prefix_length + 1) // 2 * -1:-1]
    else:
        return text

### Unit tests below ###
def check(candidate):
    assert candidate('happy', 'ha') == ''

def test_check():
    check(f)