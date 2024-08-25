import string

def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    if text and text.isupper():
        cs = str.maketrans(string.ascii_uppercase, string.ascii_lowercase)
        return text.translate(cs)
    return text.lower()[:3]

### Unit tests below ###
def check(candidate):
    assert candidate('mTYWLMwbLRVOqNEf.oLsYkZORKE[Ko[{n') == 'mty'

def test_check():
    check(f)