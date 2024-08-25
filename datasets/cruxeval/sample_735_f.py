def f(sentence: str) -> str:
    """"""
    ### Canonical solution below ###
    if sentence == '':
        return ''
    sentence = sentence.replace('(', '')
    sentence = sentence.replace(')', '')
    return sentence.capitalize().replace(' ', '')

### Unit tests below ###
def check(candidate):
    assert candidate('(A (b B))') == 'Abb'

def test_check():
    check(f)