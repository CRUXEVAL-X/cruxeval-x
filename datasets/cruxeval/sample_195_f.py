def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    for p in ['acs', 'asp', 'scn']:
        text = text.removeprefix(p) + ' '
    return text.removeprefix(' ')[:-1]

### Unit tests below ###
def check(candidate):
    assert candidate('ilfdoirwirmtoibsac') == 'ilfdoirwirmtoibsac  '

def test_check():
    check(f)