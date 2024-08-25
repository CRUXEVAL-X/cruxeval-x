def f(forest: str, animal: str) -> str:
    """"""
    ### Canonical solution below ###
    index = forest.index(animal)
    result = list(forest)
    while index < len(forest)-1:
        result[index] = forest[index+1]
        index += 1
    if index == len(forest)-1:
        result[index] = '-'
    return ''.join(result)

### Unit tests below ###
def check(candidate):
    assert candidate('2imo 12 tfiqr.', 'm') == '2io 12 tfiqr.-'

def test_check():
    check(f)