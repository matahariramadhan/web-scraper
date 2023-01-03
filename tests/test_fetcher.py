import requests
import pathlib
import pytest
from web_scraper import fetcher


@pytest.fixture
def sample_path():
    return str(pathlib.Path('tests/samples/markup.html').resolve())


@pytest.fixture
def markup(sample_path) -> bytes:
    with pathlib.Path(sample_path).open('rb') as file:
        return file.read()


@pytest.fixture
def url() -> str:
    return 'https://shamela.ws/book/23599/612'


class MockRequests:
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


def test_can_fetch_html_from_local(markup, sample_path):

    expected = markup
    actual = fetcher.Fetcher().fetch_from_local(sample_path)

    assert actual == expected


def test_can_extract_html(tmp_path, sample_path, markup):
    temp_dir = tmp_path / 'tests'
    temp_dir.mkdir()
    temp_dir = temp_dir / 'samples'
    temp_dir.mkdir()

    f = fetcher.Fetcher()
    f.fetch_from_local(sample_path)
    f.extract_html(str(temp_dir))

    file_path = pathlib.Path(temp_dir/'result.html')

    expected = markup
    actual = ''
    with file_path.open('rb') as file:
        actual = file.read()

    assert pathlib.Path(temp_dir/'result.html').exists()
    assert actual == expected
