def f(text: str, suffix: str, num: int) -> bool:
    """"""
    ### Canonical solution below ###
    str_num = str(num)
    return text.endswith(suffix + str_num)

### Unit tests below ###
def check(candidate):
    assert candidate('friends and love', 'and', 3) == False

def test_check():
    check(f)