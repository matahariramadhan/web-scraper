import pathlib
import pytest
from web_scraper import ShamelaParser


class TestShamelaParser:
    @pytest.fixture
    def markup(self) -> str:
        raw_html: str = ''

        with pathlib.Path('tests/samples/markup.html').open('r') as file:
            raw_html = file.read()
        return raw_html

    @pytest.fixture
    def shamela_parser(self, markup) -> ShamelaParser:
        shamela_parser = ShamelaParser()
        shamela_parser.parse_content(markup)
        return shamela_parser

    def test_can_parse_page_number(self, shamela_parser):
        actual = shamela_parser.page_number
        expected = '621'

        assert actual == expected

    def test_can_parse_fihris(self, shamela_parser):
        actual = shamela_parser.fihris
        expected = {
            'فهرس الكتاب': {
                'من سورة لقمان': '[سورة لقمان (٣١) : الآيات ١٤ إلى ١٥]'
            }
        }
        assert actual == expected

    def test_can_parse_hamesh(self, shamela_parser):
        actual = shamela_parser.hamesh
        expected = {
            1: '(١) في كتابه أحكام القرآن (٣/ ٣٥١) .',
            2: '(٢) الهداية شرح بداية المبتدي للإمام المرغيناني (١- ٢/ ٢٤٣) .'
        }

        assert actual == expected
