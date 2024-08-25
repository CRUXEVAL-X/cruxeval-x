def f(text: str, changes: str) -> str:
    """"""
    ### Canonical solution below ###
    result = ''
    count = 0
    changes = list(changes)
    for char in text:
        result += char if char in 'e' else changes[count % len(changes)]
        count += (1 if char not in 'e' else 0)
    return result

### Unit tests below ###
def check(candidate):
    assert candidate('fssnvd', 'yes') == 'yesyes'

def test_check():
    check(f)