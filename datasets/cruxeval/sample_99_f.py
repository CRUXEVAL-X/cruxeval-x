def f(text: str, sep: str, num: int) -> str:
    """"""
    ### Canonical solution below ###
    return '___'.join(text.rsplit(sep, num))

### Unit tests below ###
def check(candidate):
    assert candidate('aa+++bb', '+', 1) == 'aa++___bb'

def test_check():
    check(f)