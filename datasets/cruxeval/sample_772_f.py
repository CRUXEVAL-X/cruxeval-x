def f(phrase: str) -> str:
    """"""
    ### Canonical solution below ###
    result = ''
    for i in phrase:
        if not i.islower():
            result += i
    return result

### Unit tests below ###
def check(candidate):
    assert candidate('serjgpoDFdbcA.') == 'DFA.'

def test_check():
    check(f)