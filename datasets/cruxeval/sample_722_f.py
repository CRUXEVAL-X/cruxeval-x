def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    out = ""
    for i in range(len(text)):
        if text[i].isupper():
            out += text[i].lower()
        else:
            out += text[i].upper()
    return out

### Unit tests below ###
def check(candidate):
    assert candidate(',wPzPppdl/') == ',WpZpPPDL/'

def test_check():
    check(f)