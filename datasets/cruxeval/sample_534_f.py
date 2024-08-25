def f(sequence: str, value: str) -> str:
    """"""
    ### Canonical solution below ###
    i = max(sequence.index(value) - len(sequence) // 3, 0)
    result = ''
    for j, v in enumerate(sequence[i:]):
        if v == '+':
            result += value
        else:
            result += sequence[i + j]
    return result

### Unit tests below ###
def check(candidate):
    assert candidate('hosu', 'o') == 'hosu'

def test_check():
    check(f)