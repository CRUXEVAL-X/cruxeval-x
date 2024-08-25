def f(text: str, m: int, n: int) -> str:
    """"""
    ### Canonical solution below ###
    text = "{}{}{}".format(text, text[:m], text[n:])
    result = ""
    for i in range(n, len(text)-m):
        result = text[i] + result
    return result

### Unit tests below ###
def check(candidate):
    assert candidate("abcdefgabc", 1, 2) == 'bagfedcacbagfedc'

def test_check():
    check(f)