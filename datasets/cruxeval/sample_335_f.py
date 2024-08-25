def f(text: str, to_remove: str) -> str:
    """"""
    ### Canonical solution below ###
    new_text = list(text)
    if to_remove in new_text:
        index = new_text.index(to_remove)
        new_text.remove(to_remove)
        new_text.insert(index, '?')
        new_text.remove('?')
    return ''.join(new_text)

### Unit tests below ###
def check(candidate):
    assert candidate('sjbrlfqmw', 'l') == 'sjbrfqmw'

def test_check():
    check(f)