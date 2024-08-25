from typing import Dict, Union

def f(student_marks: Dict[str, int], name: str) -> Union[int, str]:
    """"""
    ### Canonical solution below ###
    if name in student_marks:
        value = student_marks.pop(name)
        return value
    return 'Name unknown'

### Unit tests below ###
def check(candidate):
    assert candidate({'882afmfp': 56}, '6f53p') == 'Name unknown'

def test_check():
    check(f)