from typing import List

def f(text: str) -> List[str]:
    """"""
    ### Canonical solution below ###
    new_text = []
    for i in range(len(text) // 3):
        new_text.append(f"< {text[i * 3: i * 3 + 3]} level={i} >")
    last_item = text[len(text) // 3 * 3:]
    new_text.append(f"< {last_item} level={len(text) // 3} >")
    return new_text

### Unit tests below ###
def check(candidate):
    assert candidate('C7') == ['< C7 level=0 >']

def test_check():
    check(f)