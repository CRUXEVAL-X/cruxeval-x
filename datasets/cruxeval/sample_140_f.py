def f(st: str) -> str:
    """"""
    ### Canonical solution below ###
    if st.lower().rindex('h', st.lower().rindex('i')) >= st.lower().rindex('i'):
        return 'Hey'
    else:
        return 'Hi'

### Unit tests below ###
def check(candidate):
    assert candidate('Hi there') == 'Hey'

def test_check():
    check(f)