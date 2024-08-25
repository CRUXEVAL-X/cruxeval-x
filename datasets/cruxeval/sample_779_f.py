def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    values = text.split()
    return '${first}y, ${second}x, ${third}r, ${fourth}p' % dict({
        'first': values[0],
        'second': values[1],
        'third': values[2],
        'fourth': values[3]
    })

### Unit tests below ###
def check(candidate):
    assert candidate('python ruby c javascript') == '${first}y, ${second}x, ${third}r, ${fourth}p'

def test_check():
    check(f)