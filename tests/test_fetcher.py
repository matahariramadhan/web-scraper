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


class TestExtractHtml:
    @pytest.fixture
    def temp_dir(self, tmp_path) -> str:
        temp_dir = tmp_path / 'tests'
        temp_dir.mkdir()
        temp_dir = temp_dir / 'samples'
        temp_dir.mkdir()
        return str(temp_dir)

    def test_can_extract_html(self, temp_dir, sample_path, markup):
        f = fetcher.Fetcher()
        f.fetch_from_local(sample_path)
        f.extract_html(str(temp_dir))

        file_path = pathlib.Path(temp_dir+'/'+'result.html')

        expected = markup
        actual = ''
        with file_path.open('rb') as file:
            actual = file.read()

        assert pathlib.Path(temp_dir+'/'+'result.html').exists()
        assert actual == expected

    def test_extract_html_raise_exception(self, temp_dir):
        with pytest.raises(Exception):
            f = fetcher.Fetcher()
            f.extract_html(temp_dir)
