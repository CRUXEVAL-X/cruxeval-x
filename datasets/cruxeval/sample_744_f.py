def f(text: str, new_ending: str) -> str:
    """"""
    ### Canonical solution below ###
    result = list(text)
    result.extend(new_ending)
    return ''.join(result)

### Unit tests below ###
def check(candidate):
    assert candidate('jro', 'wdlp') == 'jrowdlp'

def test_check():
    check(f)