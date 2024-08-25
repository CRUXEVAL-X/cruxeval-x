def f(text: str, to_place: str) -> str:
    """"""
    ### Canonical solution below ###
    after_place = text[:text.find(to_place, 0) + 1]
    before_place = text[text.find(to_place, 0) + 1:]
    return after_place + before_place

### Unit tests below ###
def check(candidate):
    assert candidate('some text', 'some') == 'some text'

def test_check():
    check(f)