from typing import Tuple

def f(text: str) -> Tuple[str, str]:
    """"""
    ### Canonical solution below ###
    topic, sep, problem = text.rpartition('|')
    if problem == 'r':
        problem = topic.replace('u', 'p')
    return topic, problem

### Unit tests below ###
def check(candidate):
    assert candidate('|xduaisf') == ('', 'xduaisf')

def test_check():
    check(f)