def f(name: str) -> str:
    """"""
    ### Canonical solution below ###
    new_name =''
    name = name[::-1]
    for i in range(len(name)):
        n = name[i]
        if n !='.' and  new_name.count('.')<2:
            new_name=n+new_name
        else:
            break
    return new_name

### Unit tests below ###
def check(candidate):
    assert candidate('.NET') == 'NET'

def test_check():
    check(f)