def f(text: str, sep: str, maxsplit: int) -> str:
    """"""
    ### Canonical solution below ###
    splitted = text.rsplit(sep, maxsplit)
    length = len(splitted)
    new_splitted = splitted[:length // 2]
    new_splitted.reverse()
    new_splitted += splitted[length // 2:]
    return sep.join(new_splitted)

### Unit tests below ###
def check(candidate):
    assert candidate('ertubwi', 'p', 5) == 'ertubwi'

def test_check():
    check(f)