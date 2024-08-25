def f(st: str) -> str:
    """"""
    ### Canonical solution below ###
    if st[0] == '~':
        e = st.rjust(10, 's')
        return f(e)
    else:
        return st.rjust(10, 'n')

### Unit tests below ###
def check(candidate):
    assert candidate('eqe-;ew22') == 'neqe-;ew22'

def test_check():
    check(f)