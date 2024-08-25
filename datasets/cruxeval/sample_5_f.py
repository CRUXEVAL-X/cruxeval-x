from typing import Tuple

def f(text: str, lower: str, upper: str) -> Tuple[int, str]:
    """"""
    ### Canonical solution below ###
    count = 0
    new_text = list()
    for char in text:
        char = lower if char.isdecimal() else upper
        if char in ['p', 'C']:
            count += 1
        new_text.append(char)
    return count, ''.join(new_text)

### Unit tests below ###
def check(candidate):
    assert candidate('DSUWeqExTQdCMGpqur', 'a', 'x') == (0, 'xxxxxxxxxxxxxxxxxx')

def test_check():
    check(f)