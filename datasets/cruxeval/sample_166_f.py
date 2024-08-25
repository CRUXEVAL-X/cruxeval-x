from typing import Dict

def f(graph: Dict[str, Dict[str, str]]) -> Dict[str, Dict[str, str]]:
    """"""
    ### Canonical solution below ###
    new_graph = {}
    for key, value in graph.items():
        new_graph[key] = {}
        for subkey in value:
            new_graph[key][subkey] = ''
    return new_graph

### Unit tests below ###
def check(candidate):
    assert candidate({}) == {}

def test_check():
    check(f)