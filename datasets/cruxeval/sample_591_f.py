from typing import List, Tuple

def f(arr: List[int]) -> Tuple[List[int], List[int]]:
    """"""
    ### Canonical solution below ###
    counts = [0] * 9 
    ans = [] 
    for ele in arr: counts[ele - 1] += 1 
    for i in range(len(counts)): 
        while counts[i] > 0: 
            counts[i] -= 1 
            ans.append(i + 1)
    return counts, ans

### Unit tests below ###
def check(candidate):
    assert candidate([6, 3, 0, 7, 4, 8]) == ([0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 4, 6, 7, 8, 9])

def test_check():
    check(f)