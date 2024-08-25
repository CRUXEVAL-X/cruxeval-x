def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    result = ''
    for char in text:
        if char.isalnum():
            result += char.upper()
    return result

### Unit tests below ###
def check(candidate):
    assert candidate('с bishop.Swift') == 'СBISHOPSWIFT'

def test_check():
    check(f)