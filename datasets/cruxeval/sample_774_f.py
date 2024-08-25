def f(num: int, name: str) -> str:
    """"""
    ### Canonical solution below ###
    f_str = 'quiz leader = {}, count = {}'
    return f_str.format(name, num)

### Unit tests below ###
def check(candidate):
    assert candidate(23, 'Cornareti') == 'quiz leader = Cornareti, count = 23'

def test_check():
    check(f)