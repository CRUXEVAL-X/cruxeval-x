def f(sentences: str) -> str:
    """"""
    ### Canonical solution below ###
    if all([sentence.isdecimal() for sentence in sentences.split('.')]):
        return 'oscillating' 
    else:
        return 'not oscillating'

### Unit tests below ###
def check(candidate):
    assert candidate('not numbers') == 'not oscillating'

def test_check():
    check(f)