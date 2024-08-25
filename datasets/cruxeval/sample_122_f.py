def f(string: str) -> str:
    """"""
    ### Canonical solution below ###
    if string[:4] != 'Nuva':
        return 'no'
    else:
        return string.rstrip()

### Unit tests below ###
def check(candidate):
    assert candidate('Nuva?dlfuyjys') == 'Nuva?dlfuyjys'

def test_check():
    check(f)