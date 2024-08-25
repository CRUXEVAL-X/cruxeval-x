def f(text: str) -> int:
    """"""
    ### Canonical solution below ###
    m = 0
    cnt = 0
    for i in text.split():
        if len(i) > m:
            cnt += 1
            m = len(i)
    return cnt

### Unit tests below ###
def check(candidate):
    assert candidate("wys silak v5 e4fi rotbi fwj 78 wigf t8s lcl") == 2

def test_check():
    check(f)