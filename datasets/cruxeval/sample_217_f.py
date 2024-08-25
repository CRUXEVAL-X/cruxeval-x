def f(string: str) -> str:
    """"""
    ### Canonical solution below ###
    if string.isalnum():
        return "ascii encoded is allowed for this language"
    return "more than ASCII"

### Unit tests below ###
def check(candidate):
    assert candidate('Str zahrnuje anglo-ameriæske vasi piscina and kuca!') == 'more than ASCII'

def test_check():
    check(f)