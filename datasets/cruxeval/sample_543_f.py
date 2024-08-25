def f(item: str) -> str:
    """"""
    ### Canonical solution below ###
    modified = item.replace('. ', ' , ').replace('&#33; ', '! ').replace('. ', '? ').replace('. ', '. ')
    return modified[0].upper() + modified[1:]

### Unit tests below ###
def check(candidate):
    assert candidate('.,,,,,. منبت') == '.,,,,, , منبت'

def test_check():
    check(f)