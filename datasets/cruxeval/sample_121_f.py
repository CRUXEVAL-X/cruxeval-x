def f(s: str) -> str:
    """"""
    ### Canonical solution below ###
    nums = ''.join(filter(lambda c:c.isdecimal(), s))
    if nums == '': return 'none'
    m = max([int(num) for num in nums.split(',')])
    return str(m)

### Unit tests below ###
def check(candidate):
    assert candidate('01,001') == '1001'

def test_check():
    check(f)