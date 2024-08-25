def f(replace: str, text: str, hide: str) -> str:
    """"""
    ### Canonical solution below ###
    while hide in text:
        replace += 'ax'
        text = text.replace(hide, replace, 1)
    return text

### Unit tests below ###
def check(candidate):
    assert candidate('###', "ph>t#A#BiEcDefW#ON#iiNCU", '.') == 'ph>t#A#BiEcDefW#ON#iiNCU'

def test_check():
    check(f)