import pathlib
from web_scraper.saver import XMLSaver
import pytest


# @pytest.fixture
# def initiate_xml_saver(autouse=True):
#     return XMLSaver()

@pytest.fixture
def dictionary():
    return {
        'page': {
            'page_number': 1,
            'fihris': {
                1: 'coba',
                2: 'aja'
            }
        }
    }


@pytest.fixture
def xml():
    return '<scraper><page><page_number>1</page_number><fihris><1>coba</1><2>aja</2></fihris></page></scraper>'


def test_xml_saver_can_save(dictionary, xml, tmp_path):
    XMLSaver(dictionary, 'scraper').save(str(tmp_path))

    actual = ''
    with pathlib.Path(tmp_path/'result.xml').open('r') as file:
        actual = file.read()
    expected = xml

    assert pathlib.Path(tmp_path/'result.xml').exists()
    assert actual == expected
