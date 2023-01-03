import pytest
from web_scraper.helper import convert_list_to_dict


@pytest.fixture
def data():
    return ['a', 'b', 'c', 'd']


def test_convert_list_to_dict(data):
    actual = convert_list_to_dict(data)
    expected = {
        'a': {
            'b': {
                'c': 'd'
            }
        }
    }

    assert actual == expected
