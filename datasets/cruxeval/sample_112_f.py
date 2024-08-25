def f(sentence: str) -> str:
    """"""
    ### Canonical solution below ###
    ls = list(sentence)
    for letter in ls:
        if not letter.istitle():
            ls.remove(letter)
    return ''.join(ls)

### Unit tests below ###
def check(candidate):
    assert candidate('XYZ LittleRedRidingHood LiTTleBIGGeXEiT fault') == 'XYZLtRRdnHodLTTBIGGeXET fult'

def test_check():
    check(f)