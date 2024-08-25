def f(text: str) -> int:
    """"""
    ### Canonical solution below ###
    return len(text) - text.count('bot')

### Unit tests below ###
def check(candidate):
    assert candidate("Where is the bot in this world?") == 30

def test_check():
    check(f)