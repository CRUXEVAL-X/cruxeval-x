def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    return text[-1] + text[:-1]

### Unit tests below ###
def check(candidate):
    assert candidate('hellomyfriendear') == 'rhellomyfriendea'

def test_check():
    check(f)