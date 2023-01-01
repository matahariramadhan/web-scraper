import pathlib
import requests
from bs4 import BeautifulSoup


class Fetcher:
    '''Fetch raw html from internet or local'''

    def fetch_from_internet(self, url) -> bytes:
        '''Return raw bytes of html from internet'''

        return requests.get(url).content

    def fetch_from_local(self, path: str) -> bytes:
        '''Return raw bytes of html from local'''
        pass

    def extract_html(self, output_path: str, output_filename: str = 'result.html') -> None:
        '''Save html to output_path/output_filename.html (result.html by default)

        The result is sanitize with beautiful soup html parser'''
        html = BeautifulSoup(self.markup, 'html.parser').prettify()
        with pathlib.Path(output_path+'/'+output_filename).open('w') as file:
            file.write(html)
