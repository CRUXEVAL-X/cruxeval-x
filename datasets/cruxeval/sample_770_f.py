def f(line: str, char: str) -> str:
    """"""
    ### Canonical solution below ###
    count = line.count(char)
    for i in range(count+1, 0, -1):
        line = line.center(len(line)+i // len(char), char)
    return line

### Unit tests below ###
def check(candidate):
    assert candidate('$78', '$') == '$$78$$'

def test_check():
    check(f)