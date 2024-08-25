def f(text: str, ch: str) -> int:
    """"""
    ### Canonical solution below ###
    """Counting vowels in Pirates' Curse"""
    return text.count(ch)

### Unit tests below ###
def check(candidate):
    assert candidate("This be Pirate's Speak for 'help'!", ' ') == 5

def test_check():
    check(f)