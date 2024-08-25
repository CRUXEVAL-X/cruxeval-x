def f(names: str) -> str:
    """"""
    ### Canonical solution below ###
    parts = names.split(',')
    for i, part in enumerate(parts):
        parts[i] = part.replace(' and', '+').title().replace('+', ' and')
    return ', '.join(parts)

### Unit tests below ###
def check(candidate):
    assert candidate("carrot, banana, and strawberry") == 'Carrot,  Banana,  and Strawberry'

def test_check():
    check(f)