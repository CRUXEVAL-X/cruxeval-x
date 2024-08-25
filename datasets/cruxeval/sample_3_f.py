def f(text: str, value: str) -> str:
    """"""
    ### Canonical solution below ###
    text_list = list(text)
    text_list.append(value)
    return ''.join(text_list)

### Unit tests below ###
def check(candidate):
    assert candidate('bcksrut', 'q') == 'bcksrutq'

def test_check():
    check(f)