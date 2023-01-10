from abc import ABC, abstractmethod
import pathlib
from xml.etree import ElementTree as ET
from web_scraper.helper import dict_to_xml


class Saver(ABC):
    '''Abstract class (interface) of all saver class'''
    @abstractmethod
    def save():
        '''Save the parsed datas'''


class XMLSaver(Saver):
    '''Saver to save to .xml file'''

    def save(self, content: dict, output_path: str, output_filename: str = 'result', root: str = 'scraper') -> None:
        root = ET.Element(root)
        root = dict_to_xml(content, root)
        tree = ET.ElementTree(root)
        with open(str(pathlib.Path(output_path).resolve())+'/'+output_filename+'.xml', 'wb') as file:
            tree.write(file, encoding='utf-8')
