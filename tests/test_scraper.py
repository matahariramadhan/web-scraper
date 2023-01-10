import pathlib
import pytest
from web_scraper import Scraper, Fetcher, ShamelaParser, XMLSaver


@pytest.fixture
def setup_scraper() -> Scraper:
    return Scraper(Fetcher, ShamelaParser, XMLSaver)


class MockFetcher:
    def fetch(self, markup) -> bytes:
        return markup


def test_fetch_from_internet_populate_self_markup(setup_scraper, monkeypatch, markup):
    s: Scraper = setup_scraper

    def mock_fetcher(*args, **kwargs):
        return MockFetcher().fetch(markup)

    monkeypatch.setattr(Fetcher, 'fetch_from_internet', mock_fetcher)
    s.fetch_from_internet('https://dummyurl.dummy')

    actual = s.markup
    expected = markup

    assert actual == expected


def test_fetch_from_local_populate_self_markup(setup_scraper, monkeypatch, markup):
    s: Scraper = setup_scraper

    def mock_fetcher(*args, **kwargs):
        return MockFetcher().fetch(markup)

    monkeypatch.setattr(Fetcher, 'fetch_from_local', mock_fetcher)
    s.fetch_from_local('/dummy/path')

    actual = s.markup
    expected = markup

    assert actual == expected


def test_parse_content_populate_self_content(setup_scraper, monkeypatch):
    s: Scraper = setup_scraper

    content = {'a': {'b': 'c'}}

    def mock_parse_content(*args, **kwargs):
        return content

    monkeypatch.setattr(ShamelaParser, 'parse_content', mock_parse_content)

    actual = s.parse_content().content
    expected = content

    assert actual == expected


def test_save_can_output_xml_file(setup_scraper, monkeypatch, tmp_path):
    s: Scraper = setup_scraper

    xml = '<a><b>c</b></a>'
    output_file = tmp_path/'result.xml'

    def mock_save(*args, **kwargs):
        with pathlib.Path(output_file).open('w') as file:
            file.write(xml)
        # return MockSaver()

    monkeypatch.setattr(XMLSaver, 'save', mock_save)
    s.save(tmp_path, 'result')

    actual: str
    with pathlib.Path(output_file).open('r') as file:
        actual = file.read()

    expected = xml

    assert actual == expected
