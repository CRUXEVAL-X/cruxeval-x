def f(s: str, p: str) -> str:
    """"""
    ### Canonical solution below ###
    arr = s.partition(p)
    part_one, part_two, part_three = len(arr[0]), len(arr[1]), len(arr[2])
    if part_one >= 2 and part_two <= 2 and part_three >= 2:
        return (arr[0][::-1] + arr[1] + arr[2][::-1] + '#')
    return (arr[0] + arr[1] + arr[2])

### Unit tests below ###
def check(candidate):
    assert candidate("qqqqq", "qqq") == 'qqqqq'

def test_check():
    check(f)