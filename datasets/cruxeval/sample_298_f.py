def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    new_text = list(text)
    for i in range(len(new_text)):
        character = new_text[i]
        new_character = character.swapcase()
        new_text[i] = new_character
    return ''.join(new_text)

### Unit tests below ###
def check(candidate):
    assert candidate('dst vavf n dmv dfvm gamcu dgcvb.') == 'DST VAVF N DMV DFVM GAMCU DGCVB.'

def test_check():
    check(f)