def f(text: str) -> str:
    """"""
    ### Canonical solution below ###
    for item in text.split():
        text = text.replace('-{}'.format(item), ' ').replace('{}-'.format(item), ' ')
    return text.strip('-')

### Unit tests below ###
def check(candidate):
    assert candidate('-stew---corn-and-beans-in soup-.-') == 'stew---corn-and-beans-in soup-.'

def test_check():
    check(f)