import pathlib
from bs4 import BeautifulSoup, Tag
from .fetcher import Fetcher
from xml.etree import ElementTree as ET


class ShamelaScraper(Fetcher):
    def __init__(self) -> None:
        super().__init__()
        self.page_number = ''
        self.hamesh = []
        self.fihris = []
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
            for i, f in enumerate(fihrises):
                if i != 0:
                    self.fihris.append(f.string)

    def __parse_nass(self, tag: Tag):
        nasses = tag.find('div', class_='nass').find_all('p')

        if len(nasses) != 0:
            for i, n in enumerate(nasses):
                if i != len(nasses)-1:
                    self.nass.append(str(n))

    def parse_from_url(self, url: str):
        raw = self.extract_raw_html(url)
        soup = BeautifulSoup(raw, 'html.parser')

        content = soup.find('div', class_='nass').parent
        self.__parse_nass(content)
        self.__parse_fihris(content)
        self.__parse_page_number(content)
        self.__parse_hamesh(content)
        return self

    def parse_from_path(self):
        pass

    def save_to_xml(self, output_path: str, output_filename: str = 'result.xml'):
        root = ET.Element('shamela')

        ET.SubElement(root, 'page_number').text = self.page_number

        fihris = ET.SubElement(root, 'fihris')
        for i, f in enumerate(self.fihris):
            ET.SubElement(fihris, str(i+1)).text = self.fihris[i]

        nass = ET.SubElement(root, 'nass')
        for i, n in enumerate(self.nass):
            ET.SubElement(nass, str(i+1)).text = self.nass[i]

        hamesh = ET.SubElement(root, 'hamesh')
        for i, h in enumerate(self.hamesh):
            ET.SubElement(hamesh, str(i+1)).text = self.hamesh[i]

        tree = ET.ElementTree(root)
        with open(str(pathlib.Path(output_path).resolve())+'/'+output_filename, 'wb') as file:
            tree.write(file, encoding='utf-8')
