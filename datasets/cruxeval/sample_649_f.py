def f(text: str, tabsize: int) -> str:
    """"""
    ### Canonical solution below ###
    return '\n'.join([
    	t.expandtabs(tabsize)
        for t in text.split('\n')
    ])

### Unit tests below ###
def check(candidate):
    assert candidate("\tf9\n\tldf9\n\tadf9!\n\tf9?", 1) == ' f9\n ldf9\n adf9!\n f9?'

def test_check():
    check(f)