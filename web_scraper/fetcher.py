import pathlib
import requests
from bs4 import BeautifulSoup


class Fetcher:
    '''Fetch raw html from internet or local and populate self.markup.

    self.markup is actual markup that fetched, it initially blank.'''

    def __init__(self) -> None:
        self.markup = ''

    def fetch_from_internet(self, url) -> bytes:
        '''Return raw bytes of html and populate self.markup from internet'''
        self.markup = requests.get(url).content
        return self.markup

    def fetch_from_local(self, path: str) -> bytes:
        '''Return raw bytes of html and populate self.markup from local'''
        with pathlib.Path(path).open('rb') as file:
            self.markup = file.read()
        return self.markup

    def extract_html(self, output_path: str, output_filename: str = 'result.html') -> None:
        '''Save self.markup to output_path/output_filename.html (result.html by default)'''
        if self.markup == '':
            raise Exception('Please fetch the html first before extracting it')

        with pathlib.Path(output_path+'/'+output_filename).open('wb') as file:
            file.write(self.markup)
