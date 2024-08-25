def f(label1: str, char: str, label2: str, index: int) -> str:
    """"""
    ### Canonical solution below ###
    m = label1.rindex(char)
    if m >= index:
        return label2[:m - index + 1]
    return label1 + label2[index - m - 1:]

### Unit tests below ###
def check(candidate):
    assert candidate('ekwies', 's', 'rpg', 1) == 'rpg'

def test_check():
    check(f)