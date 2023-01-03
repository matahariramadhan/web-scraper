import pytest
from web_scraper.helper import list_to_hierarchical_dict


@pytest.fixture
def data():
    return ['a', 'b', 'c', 'd']


def test_convert_list_to_dict(data):
    actual = list_to_hierarchical_dict(data)
    expected = {
        'a': {
            'b': {
                'c': 'd'
            }
        }
    }

    assert actual == expected
