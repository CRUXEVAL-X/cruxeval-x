def f(book: str) -> str:
    """"""
    ### Canonical solution below ###
    a = book.rsplit(':', 1)
    if a[0].split(' ')[-1] == a[1].split(' ')[0]:
        return f(' '.join(a[0].split(' ')[:-1]) + ' ' + a[1])
    return book

### Unit tests below ###
def check(candidate):
    assert candidate("udhv zcvi nhtnfyd :erwuyawa pun") == 'udhv zcvi nhtnfyd :erwuyawa pun'

def test_check():
    check(f)