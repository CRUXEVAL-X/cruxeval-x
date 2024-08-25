def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    text = text.split(',')
    text.pop(0)
    text.insert(0, text.pop(text.index('T')))
    return 'T' + ',' + ','.join(text)

### Unit tests below ###
def check(candidate):
    assert candidate("Dmreh,Sspp,T,G ,.tB,Vxk,Cct") == 'T,T,Sspp,G ,.tB,Vxk,Cct'

def test_check():
    check(f)