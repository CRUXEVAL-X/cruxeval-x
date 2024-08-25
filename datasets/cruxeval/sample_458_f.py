def f(text: str, search_chars: str, replace_chars: str) -> str:
    """"""
    ### Canonical solution below ###
    trans_table = str.maketrans(search_chars, replace_chars)
    return text.translate(trans_table)

### Unit tests below ###
def check(candidate):
    assert candidate('mmm34mIm', 'mm3', ',po') == 'pppo4pIp'

def test_check():
    check(f)