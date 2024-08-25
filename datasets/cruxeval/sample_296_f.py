def f(url: str) -> str:
    """"""
    ### Canonical solution below ###
    return url.removeprefix('http://www.')

### Unit tests below ###
def check(candidate):
    assert candidate("https://www.www.ekapusta.com/image/url") == 'https://www.www.ekapusta.com/image/url'

def test_check():
    check(f)