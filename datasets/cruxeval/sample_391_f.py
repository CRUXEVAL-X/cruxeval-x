from typing import List

def f(students: List[str]) -> List[str]:
    """"""
    ### Canonical solution below ###
    seatlist = students
    seatlist.reverse()
    cnt = 0
    for cnt in range(len(seatlist)):
        cnt += 2
        seatlist[cnt - 1:cnt] = ['+']
    seatlist.append('+')
    return seatlist

### Unit tests below ###
def check(candidate):
    assert candidate(['r', '9']) == ['9', '+', '+', '+']

def test_check():
    check(f)