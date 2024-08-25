def f(sample: str) -> int:
    """"""
    ### Canonical solution below ###
    i = -1
    while sample.find('/', i+1) != -1:
        i = sample.find('/', i+1)
    return sample.rindex('/', 0, i)

### Unit tests below ###
def check(candidate):
    assert candidate('present/here/car%2Fwe') == 7

def test_check():
    check(f)