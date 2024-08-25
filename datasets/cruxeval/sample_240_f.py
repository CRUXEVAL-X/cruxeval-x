def f(float_number: float) -> str:
    """"""
    ### Canonical solution below ###
    number = str(float_number)
    dot = number.find('.')
    if dot != -1:
        return number[:dot] + '.' + number[dot+1:].ljust(2, '0')
    return number + '.00'

### Unit tests below ###
def check(candidate):
    assert candidate(3.121) == '3.121'

def test_check():
    check(f)