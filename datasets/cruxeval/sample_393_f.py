def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    ls = text[::-1]
    text2 = ''
    for i in range(len(ls) - 3, 0, -3):
        text2 += '---'.join(ls[i:i + 3]) + '---'
    return text2[:-3]

### Unit tests below ###
def check(candidate):
    assert candidate('scala') == 'a---c---s'

def test_check():
    check(f)