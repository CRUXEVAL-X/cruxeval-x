def f(text: str, search: str) -> int:
    """"""
    ### Canonical solution below ###
    result = text.lower()
    return result.find(search.lower())

### Unit tests below ###
def check(candidate):
    assert candidate('car hat', 'car') == 0

def test_check():
    check(f)