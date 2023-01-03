from abc import ABC, abstractmethod
from bs4 import BeautifulSoup, Tag
from web_scraper.helper import list_to_hierarchical_dict


class Parser(ABC):
    '''Abstract class (interface) for parser '''

    @abstractmethod
    def parse_content(self):
        '''Parse the content from markup'''


class ShamelaParser(Parser):
    '''Parse the content of shamela.ws site'''

    def __init__(self) -> None:
        self.page_number = ''
        self.hamesh = []
        self.fihris = {}
        self.nass = []

    def __parse_hamesh(self, tag: Tag) -> None:
        hameshs = tag.find_all('p', class_='hamesh')

        if len(hameshs) != 0:
            for i, h in enumerate(hameshs):
                if i == 0:
                    self.hamesh.append(
                        h.contents[0].string)
                self.hamesh.append(
                    h.find('br').string
                )

    def __parse_page_number(self, tag: Tag) -> None:
        page_number = tag.find(id='fld_goto_top')

        self.page_number = str(page_number.attrs['value'])

    def __parse_fihris(self, tag: Tag):
        fihrises = tag.find('div', class_='heading-title').find_all('a')

        if len(fihrises) != 0:
            content = []
            for f in fihrises:
                content.append(f.string)
            self.fihris = list_to_hierarchical_dict(content)

    def __parse_nass(self, tag: Tag):
        nasses = tag.find('div', class_='nass').find_all('p')

        if len(nasses) != 0:
            for i, n in enumerate(nasses):
                if i != len(nasses)-1:
                    self.nass.append(str(n))

    def parse_content(self, markup: bytes | str) -> dict:
        soup = BeautifulSoup(markup, 'html.parser')
        content = soup.find('div', class_='nass').parent

        self.__parse_nass(content)
        self.__parse_fihris(content)
        self.__parse_page_number(content)
        self.__parse_hamesh(content)
        return {
            'page_number': self.page_number,
            'fihris': self.fihris,
            'nass': self.nass,
            'hamesh': self.hamesh
        }
