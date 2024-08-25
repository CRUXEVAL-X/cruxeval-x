def f(text: str, suffix: str) -> str:
    """"""
    ### Canonical solution below ###
    output = text
    while text.endswith(suffix):
        output = text[:-len(suffix)]
        text = output
    return output

### Unit tests below ###
def check(candidate):
    assert candidate('!klcd!ma:ri', '!') == '!klcd!ma:ri'

def test_check():
    check(f)