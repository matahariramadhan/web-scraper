import pathlib
from cli import scrape


def test_can_parse_shamela_to_xml(tmp_path):
    tmp = tmp_path
    scrape(str(tmp))

    a = ''
    e = ''
    with open(tmp / 'result.xml', 'r') as actual:
        with open(str(
                pathlib.Path('samples/').resolve()) + '/result.xml', 'r') as expected:
            e = expected.read()
        a = actual.read()
    assert a == e
