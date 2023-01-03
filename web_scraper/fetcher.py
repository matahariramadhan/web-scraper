import pathlib
import requests
from bs4 import BeautifulSoup


class Fetcher:
    '''Fetch raw html from internet or local'''

    def __init__(self) -> None:
        self.markup = ''

    def fetch_from_internet(self, url) -> bytes:
        '''Return raw bytes of html from internet and populate self.markup with markup bytes'''
        self.markup = requests.get(url).content
        return self.markup

    def fetch_from_local(self, path: str) -> bytes:
        '''Return raw bytes of html from local and populate self.markup with markup bytes'''
        with pathlib.Path(path).open('rb') as file:
            self.markup = file.read()
        return self.markup

    def extract_html(self, output_path: str, output_filename: str = 'result.html') -> None:
        '''Save self.markup to output_path/output_filename.html (result.html by default)'''
        with pathlib.Path(output_path+'/'+output_filename).open('wb') as file:
            file.write(self.markup)
