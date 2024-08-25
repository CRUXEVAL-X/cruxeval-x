from typing import Dict, List, Union

def f(dictionary: Dict[str, List[int]], arr: List[Union[int, str]]) -> Dict[str, List[int]]:
    """"""
    ### Canonical solution below ###
    dictionary.update({arr[0]: [arr[1]]})
    if len(dictionary[arr[0]]) == arr[1]:
        dictionary[arr[0]] = arr[0]
    return dictionary

### Unit tests below ###
def check(candidate):
    assert candidate({}, ['a', 2]) == {'a': [2]}

def test_check():
    check(f)