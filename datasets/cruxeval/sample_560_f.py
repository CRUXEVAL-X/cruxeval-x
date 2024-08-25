def f(text: str) -> int:
    """"""
    ### Canonical solution below ###
    x = 0
    if text.islower():
        for c in text:
            if int(c) in list(range(90)):
                x+=1
    return x

### Unit tests below ###
def check(candidate):
    assert candidate("591237865") == 0

def test_check():
    check(f)