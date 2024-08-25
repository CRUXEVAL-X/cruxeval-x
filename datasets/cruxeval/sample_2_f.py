def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    new_text = list(text)
    for i in '+':
        if i in new_text:
            new_text.remove(i)
    return ''.join(new_text)

### Unit tests below ###
def check(candidate):
    assert candidate('hbtofdeiequ') == 'hbtofdeiequ'

def test_check():
    check(f)