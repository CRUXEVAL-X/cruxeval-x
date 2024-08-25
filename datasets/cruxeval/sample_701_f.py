from typing import List

def f(stg: str, tabs: List[str]) -> str:
    """"""
    ### Canonical solution below ###
    for tab in tabs:
        stg = stg.rstrip(tab)
    return stg

### Unit tests below ###
def check(candidate):
    assert candidate('31849 let it!31849 pass!', ['3','1','8',' ','1','9','2','d']) == '31849 let it!31849 pass!'

def test_check():
    check(f)