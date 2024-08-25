def f(text: str) -> bool:
    """"""
    ### Canonical solution below ###
    return text.isascii()

### Unit tests below ###
def check(candidate):
    assert candidate('wW의IV]HDJjhgK[dGIUlVO@Ess$coZkBqu[Ct') == False

def test_check():
    check(f)