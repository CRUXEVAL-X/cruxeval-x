def f(text: str, letter: str) -> int:
    """"""
    ### Canonical solution below ###
    counts = {}
    for char in text:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts.get(letter, 0)

### Unit tests below ###
def check(candidate):
    assert candidate('za1fd1as8f7afasdfam97adfa', '7') == 2

def test_check():
    check(f)