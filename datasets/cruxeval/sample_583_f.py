def f(text: str, ch: str) -> str:
    """"""
    ### Canonical solution below ###
    result = []
    for line in text.splitlines():
        if len(line) > 0 and line[0] == ch:
            result.append(line.lower())
        else:
            result.append(line.upper())
    return "\n".join(result)

### Unit tests below ###
def check(candidate):
    assert candidate("t\nza\na", "t") == 't\nZA\nA'

def test_check():
    check(f)