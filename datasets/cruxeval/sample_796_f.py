def f(str: str, toget: str) -> str:
    """"""
    ### Canonical solution below ###
    if str.startswith(toget): return str[len(toget):]
    else: return str

### Unit tests below ###
def check(candidate):
    assert candidate('fnuiyh', 'ni') == 'fnuiyh'

def test_check():
    check(f)