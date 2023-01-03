import pathlib
from cli import scrape


def test_can_parse_shamela_to_xml(tmp_path):
    tmp = tmp_path
    scrape('https://shamela.ws/book/23599/612', str(tmp))

    assert pathlib.Path(tmp/'result.xml').exists()
