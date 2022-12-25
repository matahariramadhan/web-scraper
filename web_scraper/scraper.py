import os
import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, url: str) -> None:
        self.url = url

    def get_raw_html(self) -> bytes:
        '''Get raw bytes of html'''
        return requests.get(self.url).content

    def parse_html(self):
        '''Parse html'''
        page = self.get_raw_html()

        soup = BeautifulSoup(page, 'html.parser')
        return soup.prettify()

    def save_to_html(self, output_folder: str, output_name='result') -> None:
        '''Parse html from url and save to output_folder with output_name'''
        with open(os.path.join(output_folder, output_name + '.html'), 'w') as file:
            file.write(self.parse_html())
