from web_scraper import validation
import pytest


@pytest.fixture
def valid_url() -> str:
    return 'https://shamela.ws/book/23599/612'


def test_validate_url_pass(valid_url):
    actual = validation.Validation().validate_url(valid_url)
    expected = 'https://shamela.ws/book/23599/612'

    assert actual == expected


def test_validate_url_raise_exception_if_status_code_is_not_200():
    with pytest.raises(Exception):
        validation.Validation().validate_url('https://shamela.ws/book/23599/6120')


def test_validate_url_raise_exception():
    with pytest.raises(Exception):
        validation.Validation().validate_url('qwdsad')
