def f(line: str) -> str:
    """"""
    ### Canonical solution below ###
    count = 0
    a = []
    for i in range(len(line)):
        count += 1
        if count%2==0:
            a.append(line[i].swapcase())
        else:
            a.append(line[i])
    return ''.join(a)

### Unit tests below ###
def check(candidate):
    assert candidate("987yhNSHAshd 93275yrgSgbgSshfbsfB") == '987YhnShAShD 93275yRgsgBgssHfBsFB'

def test_check():
    check(f)