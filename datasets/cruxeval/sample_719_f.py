def f(code: str) -> str:
    """"""
    ### Canonical solution below ###
    lines = code.split(']')
    result = []
    level = 0
    for line in lines:
        result.append(line[0] + ' ' + '  ' * level + line[1:])
        level += line.count('{') - line.count('}')
    return '\n'.join(result)

### Unit tests below ###
def check(candidate):
    assert candidate("if (x) {y = 1;} else {z = 1;}") == 'i f (x) {y = 1;} else {z = 1;}'

def test_check():
    check(f)