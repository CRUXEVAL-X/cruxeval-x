def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    return text.replace('\n', '\t')

### Unit tests below ###
def check(candidate):
    assert candidate('apples\n\t\npears\n\t\nbananas') == 'apples\t\t\tpears\t\t\tbananas'

def test_check():
    check(f)