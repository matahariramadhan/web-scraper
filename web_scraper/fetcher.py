import pathlib
import requests
from bs4 import BeautifulSoup


class Fetcher:
    def __init__(self) -> None:
        pass

    def extract_raw_html(self, url: str) -> bytes:
        '''Extract raw bytes of html'''
        return requests.get(url).content

    def extract_html(self, output_path: str, output_filename: str = 'result.html') -> None:
        '''Save html to output_path to output_filename (result.html by default)'''
        raw_html = self.extract_raw_html()
        html = BeautifulSoup(raw_html, 'html.parser').prettify()
        with open(str(pathlib.Path(output_path).resolve())+'/'+output_filename, 'w') as file:
            file.write(html)
