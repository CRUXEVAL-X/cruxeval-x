def f(text: str, prefix: str) -> str:
    """"""
    ### Canonical solution below ###
    if text.startswith(prefix):
        text = text.removeprefix(prefix)
    text = text.capitalize()
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('qdhstudentamxupuihbuztn', 'jdm') == 'Qdhstudentamxupuihbuztn'

def test_check():
    check(f)