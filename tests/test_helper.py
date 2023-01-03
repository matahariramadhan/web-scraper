import pathlib
import pytest
from web_scraper.helper import *


def test_convert_list_to_dict():
    data = ['a', 'b', 'c', 'd']
    actual = list_to_hierarchical_dict(data)
    expected = {
        'a': {
            'b': {
                'c': 'd'
            }
        }
    }

    assert actual == expected


def test_dict_to_xml(tmp_path):
    dict = {'a': {'b': 'c'}}

    actual = ''
    with pathlib.Path(tmp_path/'coba.xml').open('wb') as file:
        ET.ElementTree(dict_to_xml(dict, ET.Element('root'))
                       ).write(file, encoding='utf-8')

    with pathlib.Path(tmp_path/'coba.xml').open('r') as file:
        actual = file.read()

    expected = '<root><a><b>c</b></a></root>'

    assert actual == expected
