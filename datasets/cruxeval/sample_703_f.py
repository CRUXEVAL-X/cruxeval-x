def f(text: str, char: str) -> str:
    """"""
    ### Canonical solution below ###
    count = text.count(char*2)
    return text[count:]

### Unit tests below ###
def check(candidate):
    assert candidate('vzzv2sg', 'z') == 'zzv2sg'

def test_check():
    check(f)