def f(var: str) -> str:
    """"""
    ### Canonical solution below ###
    if var.isdigit():
        return "int"
    elif var.replace('.', '', 1).isdigit():
        return "float"
    elif var.count(' ') == len(var) - 1:
        return "str"
    elif len(var) == 1:
        return "char"
    else:
        return "tuple"

### Unit tests below ###
def check(candidate):
    assert candidate(" 99 777") == 'tuple'

def test_check():
    check(f)