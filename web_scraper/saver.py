from abc import ABC, abstractmethod
import pathlib
from xml.etree import ElementTree as ET
from web_scraper.helper import dict_to_xml


class Saver(ABC):
    @abstractmethod
    def save():
        '''Save the parsed datas'''


class XMLSaver(Saver):

    def __init__(self, content: dict, root: str = 'scraper') -> None:
        self.content = content
        self.root = root

    def save(self, output_path: str, output_filename: str = 'result.xml'):
        root = ET.Element(self.root)
        root = dict_to_xml(self.content, root)
        tree = ET.ElementTree(root)
        with open(str(pathlib.Path(output_path).resolve())+'/'+output_filename, 'wb') as file:
            tree.write(file, encoding='utf-8')
