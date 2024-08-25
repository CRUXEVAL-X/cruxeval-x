def f(text: str, use: str) -> str:
    """"""
    ### Canonical solution below ###
    return text.replace(use, '')

### Unit tests below ###
def check(candidate):
    assert candidate('Chris requires a ride to the airport on Friday.', 'a') == 'Chris requires  ride to the irport on Fridy.'

def test_check():
    check(f)