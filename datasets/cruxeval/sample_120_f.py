from typing import Dict, List

def f(countries: Dict[str, str]) -> Dict[str, List[str]]:
    """"""
    ### Canonical solution below ###
    language_country = dict()
    for country, language in countries.items():
        if language not in language_country:
            language_country[language] = []
        language_country[language].append(country)
    return language_country

### Unit tests below ###
def check(candidate):
    assert candidate({}) == {}

def test_check():
    check(f)