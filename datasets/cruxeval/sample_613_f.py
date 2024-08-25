def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    result = ''
    mid = (len(text) - 1) // 2
    for i in range(mid):
        result += text[i]
    for i in range(mid, len(text)-1):
        result += text[mid + len(text) - 1 - i]
    return result.ljust(len(text), text[-1])

### Unit tests below ###
def check(candidate):
    assert candidate('eat!') == 'e!t!'

def test_check():
    check(f)