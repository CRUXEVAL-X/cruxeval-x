def f(text: str, encoding: str) -> str:
    """"""
    ### Canonical solution below ###
    try:
        return str(text.encode(encoding))
    except LookupError:
        return str(LookupError)

### Unit tests below ###
def check(candidate):
    assert candidate('13:45:56', 'shift_jis') == "b\'13:45:56\'"

def test_check():
    check(f)