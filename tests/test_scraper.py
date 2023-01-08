import pytest
from web_scraper import Scraper, Fetcher, ShamelaParser, XMLSaver


@pytest.fixture
def setup_scraper() -> Scraper:
    return Scraper(Fetcher, ShamelaParser, XMLSaver)


class MockFetcher:
    def fetch(self, markup) -> bytes:
        return markup


class MockParser:
    pass


class MockSaver:
    pass


def test_fetch_from_internet_populate_self_content(setup_scraper, monkeypatch, markup):
    s: Scraper = setup_scraper

    def mock_fetcher(self, url):
        return MockFetcher().fetch(markup)

    monkeypatch.setattr(Fetcher, 'fetch_from_internet', mock_fetcher)
    s.fetch_from_internet('https://dummyurl.dummy')

    actual = s.markup
    expected = markup

    assert actual == expected


def test_fetch_from_local_populate_self_content(setup_scraper, monkeypatch, markup):
    s: Scraper = setup_scraper

    def mock_fetcher(self, url):
        return MockFetcher().fetch(markup)

    monkeypatch.setattr(Fetcher, 'fetch_from_local', mock_fetcher)
    s.fetch_from_local('/dummy/path')

    actual = s.markup
    expected = markup

    assert actual == expected
