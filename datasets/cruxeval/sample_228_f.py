def f(text: str, splitter: str) -> str:
    """"""
    ### Canonical solution below ###
    return splitter.join(text.lower().split())

### Unit tests below ###
def check(candidate):
    assert candidate('LlTHH sAfLAPkPhtsWP', '#') == 'llthh#saflapkphtswp'

def test_check():
    check(f)