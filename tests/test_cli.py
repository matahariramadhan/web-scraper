import pytest
import pathlib
from cli import scrape


@pytest.fixture
def xml_sample():
    with pathlib.Path('tests/samples/result.xml').open('r') as file:
        return file.read()


def test_xml_file_is_exists(tmp_path):
    tmp = tmp_path
    scrape('https://shamela.ws/book/23599/612', str(tmp))

    assert pathlib.Path(tmp/'result.xml').exists()


def test_xml(tmp_path, xml_sample):
    tmp = tmp_path
    scrape('https://shamela.ws/book/23599/612', str(tmp))

    actual = ''
    with pathlib.Path(tmp/'result.xml').open('r') as file:
        actual = file.read()

    expected = xml_sample

    assert actual == expected
