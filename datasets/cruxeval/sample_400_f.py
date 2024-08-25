def f(multi_string: str) -> str:
    """"""
    ### Canonical solution below ###
    cond_string = map(str.isascii, multi_string.split())
    if True in cond_string:
        return ', '.join(x for x in multi_string.split() if x.isascii())
    return ''

### Unit tests below ###
def check(candidate):
    assert candidate('I am hungry! eat food.') == 'I, am, hungry!, eat, food.'

def test_check():
    check(f)