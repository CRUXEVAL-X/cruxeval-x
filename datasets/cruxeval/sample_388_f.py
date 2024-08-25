def f(text: str, characters: str) -> str:
    """"""
    ### Canonical solution below ###
    character_list = list(characters) + [' ', '_']

    i = 0
    while i < len(text) and text[i] in character_list:
        i += 1

    return text[i:]

### Unit tests below ###
def check(candidate):
    assert candidate("2nm_28in", "nm") == '2nm_28in'

def test_check():
    check(f)