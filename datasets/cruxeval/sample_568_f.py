def f(num: str) -> str:
    """"""
    ### Canonical solution below ###
    letter = 1
    for i in '1234567890':
        num = num.replace(i,'')
        if len(num) == 0: break
        num = num[letter:] + num[:letter]
        letter += 1
    return num

### Unit tests below ###
def check(candidate):
    assert candidate('bwmm7h') == 'mhbwm'

def test_check():
    check(f)