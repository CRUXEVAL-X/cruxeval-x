def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    odd = ''
    even = ''
    for i, c in enumerate(text):
        if i % 2 == 0:
            even += c
        else:
            odd += c
    return even + odd.lower()

### Unit tests below ###
def check(candidate):
    assert candidate('Mammoth') == 'Mmohamt'

def test_check():
    check(f)