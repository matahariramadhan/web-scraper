import requests
import pathlib
import pytest
from web_scraper import fetcher


@pytest.fixture
def markup() -> str:
    raw_html: str = ''

    with pathlib.Path('tests/samples/markup.html').open('r') as file:
        raw_html = file.read()
    return raw_html


@pytest.fixture
def url() -> str:
    return 'https://shamela.ws/book/23599/612'


class MockRequests:
    def __init__(self) -> None:
        self.content = ''

    # @staticmethod
    def get(self, markup):
        self.content = markup
        return self


def test_can_fetch_html_content_from_url(markup, url, monkeypatch):
    def mock_get(*args, **kwargs):
        return MockRequests().get(markup)

    monkeypatch.setattr(requests, 'get', mock_get)
    expected = markup
    actual = fetcher.Fetcher().fetch_from_internet(url)

    assert expected == actual
