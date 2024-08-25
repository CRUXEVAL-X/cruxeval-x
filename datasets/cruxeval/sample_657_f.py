def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    for punct in '!.?,:;':
        if text.count(punct) > 1:
            return 'no'
        if text.endswith(punct):
            return 'no'
    return text.title()

### Unit tests below ###
def check(candidate):
    assert candidate("djhasghasgdha") == 'Djhasghasgdha'

def test_check():
    check(f)