def f(title: str) -> str:
    """"""
    ### Canonical solution below ###
    return title.lower()

### Unit tests below ###
def check(candidate):
    assert candidate('   Rock   Paper   SCISSORS  ') == '   rock   paper   scissors  '

def test_check():
    check(f)