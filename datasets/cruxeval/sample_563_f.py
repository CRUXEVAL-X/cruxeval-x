def f(text1: str, text2: str) -> int:
    """"""
    ### Canonical solution below ###
    nums = []
    for i in range(len(text2)):
        nums.append(text1.count(text2[i]))
    return sum(nums)

### Unit tests below ###
def check(candidate):
    assert candidate('jivespdcxc', 'sx') == 2

def test_check():
    check(f)