def f(text: str, amount: int) -> str:
    """"""
    ### Canonical solution below ###
    length = len(text)
    pre_text = '|'
    if amount >= length:
        extra_space = amount - length
        pre_text += ' ' * (extra_space // 2)
        return pre_text + text + pre_text
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('GENERAL NAGOOR', 5) == 'GENERAL NAGOOR'

def test_check():
    check(f)