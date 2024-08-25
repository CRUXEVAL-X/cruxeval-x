def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    text_list = [char for char in text]
    for i, char in enumerate(text_list):
        text_list[i] = char.swapcase()
    return ''.join(text_list)

### Unit tests below ###
def check(candidate):
    assert candidate('akA?riu') == 'AKa?RIU'

def test_check():
    check(f)