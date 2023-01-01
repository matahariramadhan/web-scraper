from abc import ABC, abstractmethod
import pathlib
from xml.etree import ElementTree as ET


class Saver(ABC):
    @abstractmethod
    def save():
        '''Save the parsed datas'''


class XMLSaver(Saver):

    def __init__(self, output_path: str, output_filename: str = 'result.xml') -> None:
        self.output_path = output_path
        self.output_filename = output_filename

    def dict_to_xml(self, data: dict, parent) -> ET.Element:
        for key in data:
            if type(data[key]) is dict:
                tag = ET.SubElement(parent, str(key))
                self.dict_to_xml(data[key], tag)
            else:
                tag = ET.SubElement(parent, str(key)).text = str(data[key])
        return parent

    def save(self, content: dict):
        root = ET.Element('shamela')
        root = self.dict_to_xml(content, root)
        tree = ET.ElementTree(root)
        with open(str(pathlib.Path(self.output_path).resolve())+'/'+self.output_filename, 'wb') as file:
            tree.write(file, encoding='utf-8')
