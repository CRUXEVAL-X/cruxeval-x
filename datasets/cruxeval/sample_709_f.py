def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    my_list = text.split()
    my_list.sort(reverse=True)
    return ' '.join(my_list)

### Unit tests below ###
def check(candidate):
    assert candidate('a loved') == 'loved a'

def test_check():
    check(f)